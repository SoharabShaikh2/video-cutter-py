import base64

import imageio
import moviepy.video.fx.all as vfx
import json

from moviepy.audio.AudioClip import CompositeAudioClip
from moviepy.audio.fx.volumex import volumex
from moviepy.audio.io.AudioFileClip import AudioFileClip

from moviepy.video.VideoClip import TextClip, ImageClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.video.io.VideoFileClip import VideoFileClip


def splitVideo():
    surah = "002_0020049"
    clip = VideoFileClip(surah + ".mp4")
    duration = clip.duration

    if 120 < duration < 180:
        clip1 = clip.subclip(0, round(duration / 3))
        clip1.write_videofile(surah + "-part1.mp4")
        clip2 = clip.subclip(round(duration / 3)-1, (round(duration/3)*2))
        clip2.write_videofile(surah + "-part2.mp4")
        clip3 = clip.subclip((round(duration/3)*2)-1, round(duration)-1)
        clip3.write_videofile(surah + "-part3.mp4")

    elif 60 < duration < 120:
        clip1 = clip.subclip(0, round(duration / 2))
        clip1.write_videofile(surah + "-part1.mp4")
        clip2 = clip.subclip(round(duration / 2)-1, round(duration)-1)
        clip2.write_videofile(surah + "-part2.mp4")


splitVideo()
