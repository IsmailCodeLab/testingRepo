from moviepy.editor import VideoFileClip

def convert_to_mp3(filename):
    """A function to save the audio of a video clip as an audio file."""

    if filename:
        clip = VideoFileClip(filename)
        clip.audio.write_audiofile(filename[:-4] + ".mp3")
        clip.close()
    else:
        print("Can't convert to the audio.")