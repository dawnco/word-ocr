# windows 操作鼠标键盘
# https://pypi.org/project/winput/
# 2019-08-30
#  按键代码 https://docs.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes
from winput import *
import time
import numpy
import random


class PcInput:

    # 移动鼠标
    @staticmethod
    def mouseMove(x, y):
        curr = get_mouse_pos()
        currX = curr[0]
        currY = curr[1]

        distance = numpy.sqrt(numpy.square(x - currX) + numpy.square(y - currY))

        while distance > 100:
            distance = numpy.sqrt(numpy.square(x - currX) + numpy.square(y - currY))
            currX = (int)((x + currX) / 2) + random.randint(0, 10)
            currY = (int)((y + currY) / 2) + random.randint(0, 10)
            set_mouse_pos(currX, currY)
            time.sleep(0.05)

        set_mouse_pos(x, y)

        # click_mouse_button(LEFT_MOUSE_BUTTON)
        # click_key(VK_BACK)
        #

    @staticmethod
    def mouseLeftClick():
        click_mouse_button(LEFT_MOUSE_BUTTON)

    @staticmethod
    def mouseRightClick():
        click_mouse_button(RIGTH_MOUSE_BUTTON)


a = 2
while a > 1:
    PcInput.mouseLeftClick()
    time.sleep(random.randint(0, 10) / 10)
