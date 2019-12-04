#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image
from pytesseract import image_to_string

import time
import capture
import util


def cap():
    file = "data/test.png"
    capture.capture(file)
    img = Image.open(file);
    text = image_to_string(img, lang='chi_sim')
    print(text)


def mouse():
    set_mouse_pos(90, 556)
    time.sleep(2)
    click_mouse_button(LEFT_MOUSE_BUTTON)
    # click_mouse_button(RIGHT_MOUSE_BUTTON)
    # click_key(VK_BACK)


if __name__ == '__main__':
    mouse()
