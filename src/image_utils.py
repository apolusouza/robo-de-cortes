from src.config import *

class GeradorLegenda:
  def __init__(self, texto):
    self.texto = texto

  def gerar_legenda(self,texto):
    if len(self.texto)>=100 and len(self.texto)<=150:
        text_box = textwrap.fill(self.texto, 35)
        print(text_box)
    else:
      print('Informe um texto com no mínimo 100 caracteres e no máximo 150 caracteres')


  #recebe um array e calcula e retorna o tamanho da text_box
  def size_box(self,text_box):
    array_box = text_box.split('\n')
    size_line = len(array_box[0])
    print(size_line)
    size_height = len(array_box)

    FONT_SIZE_PX = (1.3 * FONT_SIZE_PT)
    PADDING_TEXT_BOX = 20
    size_line = size_line * (FONT_SIZE_PX*0.6)
    size_height = size_height * FONT_SIZE_PX
    return size_line,size_height

  size_xy = size_box(text_box)
  print(int(size_xy[0]))

  font = ImageFont.truetype("Poppins-Regular.ttf", FONT_SIZE_PT) #padrão fonte 48
  #d.multiline_text((30, 30), texto_quebrado, fill="white", font=font)
  im = Image.new("RGBA", (int(size_xy[0]), int(size_xy[1])),'#ff000000')
  d = ImageDraw.Draw(im)
  d.multiline_text((0,0), text_box, fill="white", font=font)
  im.save('legenda.png')