from PIL import Image
from pytesseract import image_to_string

img = Image.open("test.png");
text = image_to_string(img, lang='chi_sim')
print(text)