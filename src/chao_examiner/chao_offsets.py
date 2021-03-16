"""
Lookup tables for data on Chao

Data taken from: https://chao.tehfusion.co.uk/chao-hacking/
"""

# TODO : Checking function for this data.

DATA_TYPE_LENGTHS = {
    "Byte": 1,
    "Signed byte": 1,
    "Short": 2,
    "Int": 4,
    "Float": 4,
}

CHAO_OFFSETS = {
    "Swim stat grade 1": {
        "offset": 1172,
        "data_type": "Byte",
        "lookup": "Grade",
    }
}
