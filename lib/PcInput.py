# windows 操作鼠标键盘
# https://pypi.org/project/winput/
# 2019-08-30
#  按键代码
#  https://docs.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes

import winput
import time
import numpy
import random


class PcInput:

    # 移动鼠标
    @staticmethod
    def mouseMove(x, y):
        curr = winput.get_mouse_pos()
        currX = curr[0]
        currY = curr[1]

        distance = numpy.sqrt(numpy.square(x - currX) + numpy.square(y - currY))

        while distance > 100:
            distance = numpy.sqrt(numpy.square(x - currX) + numpy.square(y - currY))
            currX = (int)((x + currX) / 2) + random.randint(0, 10)
            currY = (int)((y + currY) / 2) + random.randint(0, 10)
            winput.set_mouse_pos(currX, currY)
            time.sleep(0.05)

        winput.set_mouse_pos(x, y)

        # click_mouse_button(LEFT_MOUSE_BUTTON)
        # click_key(VK_BACK)
        #

    @staticmethod
    def mouseLeftClick():
        time.sleep(0.2)
        winput.click_key(winput.VK_CONTROL)
        time.sleep(0.2)
        winput.click_mouse_button(winput.LEFT_MOUSE_BUTTON)

    @staticmethod
    def mouseRightClick():
        winput.click_mouse_button(winput.RIGTH_MOUSE_BUTTON)


gRun = True


def keyboard_callback(event):
    global gRun
    print(event.vkCode)
    if event.vkCode == winput.VK_ESCAPE:  # quit on pressing escape
        winput.stop()
        gRun = False

winput.hook_keyboard(keyboard_callback)

while gRun:
    PcInput.mouseLeftClick()
    time.sleep(2)
