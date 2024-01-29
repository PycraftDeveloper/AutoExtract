<div align="center">
  
  ![image](https://github.com/PycraftDeveloper/AutoExtract/assets/81379254/54c76c98-7ab5-49f2-bceb-4c4060a4dbb3)
</div>

# AutoExtract

Automatically extract compressed folders in your downloads folder so you don't have to!

## About

AutoExtract, or AE for short, is a small project designed to perform a big task, its job is to manage the contents of your downloads directory, and automatically extract any compressed folders that may end up there.

## Supported files

AutoExtract has been designed to support the most common compressed folder types, including: `.zip`, `.7z`, `.tar`, `.gztar`, `bztar` and `xtar`.

## Features

* Passive directory management - Instead of checking the contents of your downloads folder over an interval, AutoExtract listens for file events and will automatically run when needed, saving resources.
* Multiple compressed file types - Allowing for the extraction of a whole range of file formats.
* Easy to install and manage - AutoExtract is just one small file, meaning you can put it wherever you want.
* Reversable - Once a file has been extracted, the compressed file is sent to the recycle bin, not delected forever.
* Automatic downloads folder detection - Like organising your folders? Well don't worry, this program will automatically detect where your downloads folder is.
* Multi-platform support - This program works on Windows and Linux (and probably other oprating systems too)
* Fast extraction - AutoExtract is faster than Window's default extraction utility, and even beats 7-Zip in some tasks.

## Installation

### Installation on Windows:
1. Head over the the releases section and grab the latest release.
2. Download the executable file.
3. Run the executable file to begin!

Optionally, you can hit `Win + R` and type `shell:startup` to place a shortcut to the executable there, then the program runs at startup.

### Installation on other oprating systems:
1. Head over to the releases section and download the source code.
2. Make sure to download and install Python.
3. Run `pip install -r requirements.txt` from a terminal inside the downloaded folder to download requirements.
4. Run the Python file!

## Prformance Comparison

