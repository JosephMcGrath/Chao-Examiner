import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "readme.md").read_text()
with open(HERE / "readme.md", encoding="utf-8") as f:
    README = f.read()

# This call to setup() does all the work
setup(
    name="chao_examiner",
    version="1.0.0",
    description="Module to load, examine and manipulate Chao data for Sonic Adventure 2 save data.",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Joe McGrath",
    license="MIT",
    classifiers=[
        # https://pypi.org/classifiers/
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: Microsoft :: Windows :: Windows 10",
    ],
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": ["chao_examiner=chao_examiner.__main__:chao_to_json"]
    },
)
