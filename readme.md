# all-to

## Introduction
_All-to_ is a script in a set of media utilities centered around automating jobs that involve invocations of _ffmpeg._ The purpose of _all-to_ is to transcode all of the files in a given folder to a codec of the user's choosing.

### Usage
```
usage: all-to.py [-h] [-f] to

Convert all audio files in folder to a specified type.

positional arguments:
  to          Codec to transcode into (file extension)

optional arguments:
  -h, --help  show this help message and exit
  -f          Folderize output
```

Example: `all-to ogg`

This will convert all audio files in the current directory to Ogg-Vorbis and output them in the same folder. It does not delete the input files.

Example: `all-to -f mp3`, `all-to mp3 -f`

This does the same, converting to mp3, but instead places them in a subdirectory by the same name as the current working directory, but with `.mp3` appended to it.

### Notes and limitations
* Any files that are already of the type specified will not be excluded.
* There is not yet any way to pass any additional arguments to _ffmpeg._ Defaults will be used.
* Only the current working directory is used as input. There is not yet any way to specify a directory for input.

## Installation
1. Make a directory to contain binaries and scripts if you do not already have one (e.g. `c:\bin`). Let this be called the _bin_ directory.
2. Make sure that directory is in the _search path._
3. Build or download _ffmpeg_ and _ffprobe_, and place the binaries in your _bin_ directory.
4. Configure your system to regard `.py` files as executables.
5. Modify the script to search in a directory that you prefer, or `os.getcwd()` to use the _current working directory_.
