from src.config import *
import textwrap
import sys
from PIL import Image, ImageFont, ImageDraw, ImageText

class GeradorLegenda:
  def __init__(self, texto):
    self.texto = texto

  #recebe um array e calcula e retorna o tamanho da text_box
  def _size_box(self):
    text = textwrap.fill(self.texto, 35)
    self.texto = text
    if len(text)>=100 and len(text)<=150:
      array_box = text.split('\n')
      size_line = len(array_box[0])
      print(size_line)
      size_height = len(array_box)

      FONT_SIZE_PX = (1.3 * FONT_SIZE_PT)
      PADDING_TEXT_BOX = 20
      size_line = size_line * (FONT_SIZE_PX*0.6)
      size_height = size_height * FONT_SIZE_PX
      return size_line,size_height
    else:
      print('Informe um texto com no mínimo 100 caracteres e no máximo 150 caracteres')

  def _create_box(self): 
    size_xy = self._size_box()

    im = Image.new("RGBA",(int(size_xy[0]), int(size_xy[1])),'#ff000000')
    font = ImageFont.truetype(FONT_PATH, FONT_SIZE_PT) #padrão fonte 48
    
    texto = ImageText.Text(self.text,font)
    
    im.text(self.texto,font)
    desenho = ImageDraw.Draw(im)
    
    print(f"Largura:{int(size_xy[0])} e Altura: {int(size_xy[1])}")
    im.save('teste.png')