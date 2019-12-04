# coding=utf-8

# 文字识别
# 2018-08-30

from PIL import Image
from pytesseract import image_to_string

name = "a1"

img = Image.open("data/" + name + ".png");
img = img.convert('L')  # convert image to black and white
img.save("data/bw-" + name + ".png")
text = image_to_string(img, lang='chi_sim')
print(text)
