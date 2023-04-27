# RAD-Downloader

A simple tool to download all the files from the Eurocontrol RAD found [here](https://www.nm.eurocontrol.int/RAD/).

## Installing

1. Install Python 3, preferably the most recent stable release.
2. Install required modules using the following command in the terminal:
```python
python -m pip install requests bs4
```

## Usage

When asked what cycle to use, leave the prompt empty to use current AIRAC or enter one of your choosing (eg. 2204).

*Eurocontrol removes RADs from cycles over 7 months old, if you are getting errors check the cycle you are requesting.*

The requested cycle will then be downloaded in the /RAD folder in the installation directory, and if a cycle has been previously downloaded, it will be backed up to /RAD_backup.

## TODO

- [x] Retrieve basic RAD documents
- [ ] Retrieve additional RAD documents
- [ ] Allow the user to choose what documents are downloaded per section
