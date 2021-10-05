import os
from PIL import Image, ImageDraw
from prettytable import PrettyTable

mypath = "./images"
t = PrettyTable(['name', 'size', 'height', 'width', 'correct?'])

expected_size = 300000 # 300kb
expect_height = 1000 # 1000px
expect_width = 1000 # 1000px

for folder, subfolder, files in os.walk(mypath):
  for file_name in files:
    file_path = os.path.join(folder, file_name)
    file_size = os.stat(file_path).st_size
    file_name_without_ext = os.path.splitext(file_name)[0]
    im = Image.open(file_path)
    width, height = im.size
    
    if file_size < expected_size and height == expect_height and width == expect_width:
      t.add_row([file_name, file_size, height, width, "yes"])
    else:
      t.add_row([file_name, file_size, height, width, "no"])

      nh, nw = expect_height, expect_width 

      wpercent = (nw/float(im.size[0]))
      hsize = int((float(im.size[1])*float(wpercent)))
      im = im.resize((nw,hsize), Image.ANTIALIAS)

      inh, inw = im.size 

      bgc_white = Image.new("RGB", (nw, nh), "white")
      bgc_white.paste(
        im, 
        (
          int(((nh - inh) / 2)),
          int(((nw - inw) / 2)) 
        )
      )      
      bgc_white.save(f"{file_name_without_ext}-resize.jpg")
print(t)