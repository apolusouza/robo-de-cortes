from src.config import *
from src.video_utils import *
from moviepy import  VideoFileClip, AudioClip, CompositeVideoClip, ImageClip

video = VideoFileClip(VIDEO_PATH)
normalize = video_normalize()

proporcao = normalize.calculate_xy_ct(video)
print(f'Proporção: {proporcao}')


