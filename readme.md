# Chao Examiner

A Python module to load, examine and manipulate Chao data for Sonic Adventure 2 save data.
In it's current state it's a read-only tool and I've not really got any plans to change that.

## Acknowledgements

This was inspired by and builds on the work of Fusion ([link](https://chao.tehfusion.co.uk/chao-hacking)).


## Installation

As this was a bit of a toy project to experiment with binary data I've not put it on pypi.
If for some reason you *do* want to install it you should be able to use:
```
pip install git+https://github.com/JosephMcGrath/chao_examiner.git#egg=chao_examiner
```


## Quick Start

The tool is largely limited to extracting data from a save file into JSON outputs.

After installation, the tool can either be run as a command line tool:
```bat
chao_examiner -source_dir "C:\Program Files (x86)\Steam\steamapps\common\Sonic Adventure 2" -output_dir "C:\Path\to\output"
```

Or in Python itself:
```py
save_file = ChaoSaveFile.find(r"C:\Program Files (x86)\Steam\steamapps\common\Sonic Adventure 2")
save_file.to_json(r"C:\Path\to\output")
```


## Editing Save Files

The functionality to edit save files is largely complete but the tool does not create working save files.
As far as I can tell this is due to some kind of check-sums that I'm not recalculating but I haven't really looked into it.

The mechanic to edit a chao is:
```py
# Load the chao (0-indexed).
chao = save_file.get_chao(0)

# Set properties - the reference data will push this back to the correct binary values.
chao["Name"] = "NewName"

# Update the save file and write it back to file.
save_file.set_chao(chao, 0)
save_file.write(temp_path_a)
```
This changes the values in the file, but the game refuses to read the resulting save file.


## TODO

1. Pretty extraction of non-chao data
    * Ideally set up to be able to work out what's going on next time I'm working with this,
2. Pull out remaining to-do items,
3. Stick it on GitHub,
