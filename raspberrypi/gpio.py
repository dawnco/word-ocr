#!/usr/bin/python
# -*- coding: UTF-8 -*-

import RPi.GPIO as GPIO  # 先要导入模块
import time

mode = GPIO.getmode()

# GPIO.setwarnings(False)

channel = 18

##BCM 对应 GPIO numbers , BOARD 对应 physical numbers。
GPIO.setmode(GPIO.BCM)  # 选择 GPIO numbers 编号系统

GPIO.setup(channel, GPIO.OUT, initial=GPIO.HIGH)
# GPIO.setup(3,GPIO.IN)     #把引脚 3 设置为输入模式

state = True

while (True):
    GPIO.output(channel, state)  # 让引脚 2 输出高电平
    state = not state
    time.sleep(1)

# 程序最后结束后，可以全部设置为输入
GPIO.cleanup()
