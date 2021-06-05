"""
Tutorial Link:https://youtu.be/k2_q-6wpyZE
"""
from moviepy.editor import VideoFileClip


def converter(filename):
    obj = VideoFileClip(filename=filename)

    obj.audio.write_audiofile(filename[:-4] + '.mp3')

    obj.close()
