
from PIL import Image
from pytesseract import image_to_string

import capture
import util



if __name__ == '__main__':
    file = "data/test.png"
    capture.capture(file)
    img = Image.open(file);
    text = image_to_string(img, lang='chi_sim')
    print(text)