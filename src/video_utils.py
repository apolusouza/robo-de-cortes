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

  def _cropped_video(self, video=None, xy_center=None, key_side=None, measure=None):
      kwargs = {
        'x_center': xy_center[0],
        'y_center': xy_center[1],
        'width': element.w,
        'height': element.h
    }
      kwargs[key_side] = measure
      if video is None:
        element = self.video
        return element.crop(**kwargs)
      else:
        return video.crop(**kwargs)  

  def _normalizar(self):
    #Largura maior que 1080 ou menor
    
    if self.video.w < WIDTH or self.video.w > WIDTH:
      width_norm = video.resize(width=WIDTH)
      if width_norm.h > HEIGHT:
        center = self._calculate_center(video=width_norm)
        return self._cropped_video(video=width_norm, xy_center=center, key_side='height', measure=HEIGHT)
    elif self.video.h < HEIGHT: #Altura menor que 400
      height_norm = self.video.resize(height=HEIGHT)
      if height_norm.w > WIDTH:
        xy_center = self._calculate_center(video=height_norm)
        return self._cropped_video(video=height_norm, xy_center=xy_center, key_side='width', measure=WIDTH)
    elif self.video.h > HEIGHT: # Altura maior que 400
      print(f'Ele É maior que {HEIGHT}')
      xy_center = self._calculate_center()
      print(xy_center[0])
      video = self._cropped_video(video=self.video, xy_center=xy_center, key_side='height', measure=HEIGHT)

      print(f'Altura: {video.h}, Largura:{video.w}')