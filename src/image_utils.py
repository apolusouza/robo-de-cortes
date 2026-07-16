from src.config import *
import textwrap
import sys
from PIL import Image, ImageFont, ImageDraw

class GeradorLegenda:
  def __init__(self, texto):
    self.texto = texto

  #recebe um array e calcula e retorna o tamanho da text_box
  def _size_box(self):
    text = textwrap.fill(self.texto, 35)
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
    print(size_xy) 
    print(int(size_xy[0]))
    font = ImageFont.truetype("Poppins-Regular.ttf", FONT_SIZE_PT) #padrão fonte 48
    
    #d.multiline_text((30, 30), texto_quebrado, fill="white", font=font)
    im = Image.new("RGBA", (int(size_line), int(size_height),'#ff000000'))
    d = ImageDraw.Draw(im)
    d.multiline_text((0,0), text_box, fill="white", font=font)
    im.save('legenda.png')