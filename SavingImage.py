import requests
from io import BytesIO
from PIL import Image

r=requests.get("https://lh3.ggpht.com/4WxObRWJFYaaK5oAqifk__g3FrbG9tJ9sfPH5PenAPFG_MW0R0pbdrqXieVRFWV2q20=h900")
print("Status Code",r.status_code)
image=Image.open(BytesIO(r.content))
print("image size:",image.size,"Image format",image.format,"Image mode:",image.mode)
path="./wallpaer2." + image.format

try:
    image.save(path,image.format)
except IOError:
    print("Image Not saved")

''' Pil is from pillow, image.save is to save image
'''