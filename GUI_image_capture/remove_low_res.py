import os
from PIL import Image

img_dir = "/home/pi/BIOE_521_Final_Project/GUI_image_capture/output"
for filename in os.listdir(img_dir):
    filepath = os.path.join(img_dir, filename)
    with Image.open(filepath) as im:
        x, y = im.size
    totalsize = x*y
    if totalsize < 307200:
        os.remove(filepath)
