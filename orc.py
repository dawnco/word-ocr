# 文字识别
# 2018-08-30

from PIL import Image
from pytesseract import image_to_string

img = Image.open("data/test.png");
img = img.convert('L')  # convert image to black and white
img.save('data/test-1.png')
text = image_to_string(img, lang='chi_sim')
print(text)
