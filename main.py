from src.config import *
from src.video_utils import * 
from moviepy import VideoFileClip, AudioClip, CompositeVideoClip, ImageClip

video = VideoFileClip(VIDEO_PATH)
normalize = VideoNormalize(video)
proporcao = normalize._center()

autenticado = normalize._normalizar()
print(f"A largura:{autenticado.w}, altura:{autenticado.h}")

texto = "Python é uma linguagem de programação de alto nível, amplamente utilizada para desenvolvimento web, análise de dados e inteligência artificial."


