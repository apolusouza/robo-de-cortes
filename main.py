from src.config import *
from src.video_utils import * 
from moviepy import VideoFileClip, AudioClip, CompositeVideoClip, ImageClip

video = VideoFileClip(VIDEO_PATH)
normalize = VideoNormalize(video)
proporcao = normalize._calculate_center()

autenticado = normalize._normalizar()
print(f'Altura: {autenticado.h}, Largura:{autenticado.w}')


