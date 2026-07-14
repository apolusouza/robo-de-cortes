class video_normalize:
  def calculate_xy_ct(element):
    x_center = element.w/2
    y_center = element.h/2
    xy_center = [x_center,y_center]
    return xy_center

  def cropped_video(element, xy_center, key_side, measure):
    kwargs = {
        'x_center': xy_center[0],
        'y_center': xy_center[1],
        'width': element.w,
        'height': element.h
    }
    kwargs[key_side] = measure
    return element.crop(**kwargs)

  def verifica():
    #Largura maior que 1080 ou menor
    if video.w < WIDTH or video.w > WIDTH:
      width_norm = video.resize(width=WIDTH)
      if width_norm.h > HEIGHT:
        xy_center = calculate_xy_ct(width_norm)
        video = cropped_video(width_norm, xy_center, 'height', HEIGHT)
    elif video.h < HEIGHT: #Altura menor que 400
      height_norm = video.resize(height=HEIGHT)
      if height_norm.w > WIDTH:
        xy_center = calculate_xy_ct(height_norm)
        video = cropped_video(height_norm,  xy_center, 'width', WIDTH)
    elif video.h > HEIGHT: # Altura maior que 400
      print(f'Ele É maior que {HEIGHT}')
      xy_center = calculate_xy_ct(video)
      print(xy_center[0])
      video = cropped_video(video, xy_center, 'height', HEIGHT)

      print(f'Altura: {video.h}, Largura:{video.w}')