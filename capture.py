# 截屏
# 
#  https://pyscreenshot.readthedocs.io/en/latest/
import time
import pyscreenshot as screenshot


# 截图
def capture(filename):# grab fullscreen
    im = screenshot.grab(bbox=(100, 100, 800, 800))
    #im = screenshot.grab()
    # save image file
    im.save(filename)


'''
if __name__ == '__main__':

    beg = time.time()
    capture("data/screenshot.png")
    end = time.time()
    print(end - beg)
'''
