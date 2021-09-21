# all-to


## Introduction
_All-to_ is a script in a set of media utilities centered around automating jobs that involve invocations of _ffmpeg._ The purpose of _all-to_ is to transcode all of the files in a given folder to a codec of the user's choosing.

### Usage
`usage: all-to.py [-h] [-f] to`

Example: `all-to ogg`

This will convert all audio files in the current directory to Ogg-Vorbis and output them in the same folder. It does not delete the input files.

Example: `all-to -f mp3`

This does the same, converting to mp3, but instead places them in a subdirectory by the same name as the current working directory, but with `.mp3` appended to it.

### Notes and limitations
* Any files that are already of the type specified will not be excluded.
* There is not yet any way to pass any additional arguments to _ffmpeg._ Defaults will be used.
* Only the current working directory is used as input. There is not yet any way to specify a directory for input.
