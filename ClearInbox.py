import pyautogui as pygui
import time
import os
pygui.FAILSAFE = False
pygui.click(x=35, y=10)
time.sleep(1)
pygui.moveTo(x=868, y=1037, duration=1)
time.sleep(1)
pygui.drag(+424, -491,duration=1)
time.sleep(10)
pygui.click(x=1292, y=546)
time.sleep(2)

#proton:
pygui.click(x=134, y=132)
time.sleep(60)
pygui.click(x=953, y=660)
time.sleep(60)
pygui.click(x=338, y=287)
time.sleep(3)
pygui.click(x=478, y=289)
time.sleep(30)

#gmail:
pygui.click(x=250, y=133)
time.sleep(5)
pygui.click(x=1796, y=183)
time.sleep(5)
pygui.click(x=1125, y=564)
pygui.click(x=1392, y=714)
time.sleep(5)
pygui.click(x=1392, y=714)
time.sleep(10)
pygui.click(x=1668, y=185)
time.sleep(60)
pygui.click(x=352, y=234)
time.sleep(3)
pygui.click(x=505, y=234)
time.sleep(10)


