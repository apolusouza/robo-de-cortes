from src.config import WIDTH, HEIGHT

class VideoNormalize:

  def __init__(self, video):
    self.video = video

  def _calculate_center(self, video=None):
    if video is None:
      video = self.video
    positions_float = [video.w/2, video.h/2]
    positions_int = []
    for position in positions_float:
      positions_int.append(int(position))
    return positions_int

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
      elif
        return media.cropped(**kwargs)
      elif:
        return media(x_center=kwargs['x_center'],key_side=measure)


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
      video = self.video.resized(height=HEIGHT)      
      if self.video != WIDTH:        
        xy_center = self._calculate_center(video=self.video)
        print(f"Largura: {video.w}, Altura: {video.h}")
        return self._cropped_video(media=video, xy_center=xy_center, key_side='width', measure=WIDTH)
  

