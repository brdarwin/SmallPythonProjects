import pyautogui as pyauto
import time


def main ():
	time.sleep(10)
	pyauto.FAILSAFE = False
	print (pyauto.position())
    
	


main ()
