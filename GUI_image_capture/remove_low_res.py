from PIL import Image

img_dir = r"C:\Users\Barney\Documents\sam"
for filename in os.listdir(img_dir):
    filepath = os.path.join(img_dir, filename)
    with Image.open(filepath) as im:
        x, y = im.size
    totalsize = x*y
    if totalsize < 2073600:
        os.remove(filepath)
