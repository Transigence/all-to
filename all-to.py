import sys, argparse
import os, subprocess

TEST = True

AUDIO_EXTENSIONS = {"aac", "flac", "mp3", "ogg", "opus", "wav"}
CODEC_LIBS = {"aac": "aac", "flac": "flac", "mp3": "libmp3lame", "ogg": "libvorbis", "opus": "libopus", "wav": "wav"} #wav is wrong. I know it is. I'll fix it later (next time I want wav output).
HELP_EPILOG="""
"""

WORK_DIR: str
DEST_DIR: str

Codec = None

def get_args():
    argparser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="Convert all audio files in folder to a specified type.",
        epilog=HELP_EPILOG
        )
    argparser.add_argument("to", type=str, nargs=1, help="Codec to transcode into (file extension)")
    argparser.add_argument("-f", action="store_true", help="Folderize output")
    return argparser.parse_args()

if __name__ == "__main__":
    WORK_DIR = os.getcwd()
    DEST_DIR = WORK_DIR

    args = get_args()
    if not args.to:
        print("You must specify a codec (by file extension) to which to convert.")
        sys.exit(1)
    else:
        Codec = args.to[0].lower()
        AUDIO_EXTENSIONS.remove(Codec)

    if args.f:
        output_folder = "%s.%s" % (os.path.split(WORK_DIR)[1], Codec)
        output_fullpath = os.path.join(WORK_DIR, output_folder)
        if os.path.exists(output_fullpath):
            if os.path.isdir(output_fullpath):
                print("Output folder already exists.")
            else:
                print("Output folder name exists, but is not a folder. Aborting.")
                sys.exit(1)
        else:
            print("Making the folder: %s." % output_fullpath)
            if not TEST:
                os.mkdir(output_fullpath)
            else:
                print("mkdir %s" % output_fullpath)

        DEST_DIR = output_fullpath

    files = os.listdir(WORK_DIR)
    job_files: list
    for f in files:
        fbase, fext = os.path.splitext(f)
        if fext[1:] in AUDIO_EXTENSIONS:
            proc = subprocess.run(["ffprobe", os.path.join(WORK_DIR, f)], capture_output = True)

            if proc.stderr.decode("UTF-8").find("Audio:") != -1:
                job_files.append(f)
            else:
                print("File \"%s\" didn't contain an audio stream. Skipping..." % f)
                continue
    for f in job_files:
        fq_input_name = os.path.join(WORK_DIR, f)
        output_name = "%s.%s" % (os.path.splitext(f)[0], Codec)
        fq_output_name = os.path.join(DEST_DIR, output_name)

        command = "ffmpeg -i " + "\"%s\"" % fq_input_name + " -c:a " + CODEC_LIBS[Codec] + " \"%s\"" % fq_output_name
        if not TEST:
            subprocess.run(command)
        else:
            print(command)
