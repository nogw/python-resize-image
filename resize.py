from PIL import Image, ImageDraw
from prettytable import PrettyTable
import os
import io

mypath = "./images"
t = PrettyTable(['name', 'size', 'height', 'width', 'adjusted?'])

expected_size = 300000 # 300kb
expected_height = 1000 # 1000px
expected_width = 1000 # 1000px

def format_size(fsize):
  if fsize > 1000000:
    size = f'{(int(fsize / 1048)):2,}'.replace(',','.')
    return f'{str(size):.4s}mb'
  else: return f"{int(fsize / 1024)}kb"

def resize_image_bytes(img_name):
  quality = 100
  while True: 
    img = Image.open(img_name)
    size = os.stat(img_name).st_size
    if size > expected_size:
      quality -= 1
      img.save(img_name, quality=quality)
    else: 
      t.add_row([img_name, format_size(size), "1000", "1000", "yes"])
      break

def resize_image(file_name, file_size, height, width, im):
  nh, nw = expected_height, expected_width 
  wpercent = (nw/float(im.size[0]))
  hsize = int((float(im.size[1])*float(wpercent)))
  im = im.resize((nw,hsize), Image.ANTIALIAS)
  inh, inw = im.size 
  bgc_white = Image.new("RGB", (nw, nh), "white")
  bgc_white.paste(im, (int(((nh - inh) / 2)), int(((nw - inw) / 2))))      
  new_name = f"{file_name_without_ext}-resize.jpg"
  bgc_white.save(new_name, quality=100)
  if os.stat(new_name).st_size > expected_size:
    resize_image_bytes(new_name)

for folder, subfolder, files in os.walk(mypath):
  for file_name in files:
    file_path = os.path.join(folder, file_name)
    file_size = os.stat(file_path).st_size
    file_name_without_ext = os.path.splitext(file_name)[0]
    im = Image.open(file_path)
    width, height = im.size
    
    if file_size < expected_size and height == expected_height and width == expected_width:
      t.add_row([file_name, file_size, height, width, "no"])
    else:
      resize_image(file_name, file_size, height, width, im)
print(t)