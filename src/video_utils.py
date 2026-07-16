from src.config import WIDTH, HEIGHT

class VideoNormalize:

  def __init__(self, video):
    self.video = video

  def _center(self, video=None):    
    def calculate_center(video):
      print(video)
      positions_float = [video.w/2, video.h/2]
      positions_int = []
      for position in positions_float:
        positions_int.append(int(position))
      return positions_int

    if video == None:
      video = self.video
      calculate_center(video)
    elif video != None:
      calculate_center(video)
  

  def _cropped_video(self, media=None, xy_center=None, key_side=None, measure=None):
      kwargs = {
        'x_center': xy_center[0],
        'y_center': xy_center[1],
        'width': media.w,
        'height': media.h
    }
      kwargs[key_side] = measure    
      if media == None:
       return self.video.cropped(**kwargs)
      elif media != None:
        return media.cropped(**kwargs)


  def _normalizar(self):
    print(self.video)
    #Largura diferente de 1080 então normalize o vvídeo
    if self.video.w != WIDTH:
      self.video.resized(width=WIDTH)
      if self.video > HEIGHT:
        center = self._calculate_center(video=self.video)
        return self._cropped_video(media=self.video, xy_center=center, key_side='height', measure=HEIGHT)
    
    #Altura diferente de 400px (menor ou maior)
    #menor aumenta com rsized - verifica se W ficou maior - ok - corta as sobras
    #maior corta parte superior e inferior retorna o objeto
    elif self.video.h < HEIGHT:
      video = self.video.resized(height=HEIGHT)
      if video.w > WIDTH:
        center = self._calculate_center(vide=video)        
        return self._cropped_video(video=video,xy_center=center[0],key_side='width',width=WIDTH)


    elif self.video.h > HEIGHT:
        print(self.video)       
        center = int(self.video.w/2)
        print(center)
        return self.video.cropped(y_center=center,height=HEIGHT)

  

