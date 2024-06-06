import pyautogui as pyg
import time
import os

def clickingArea(imgPath):
    try:
        img  = pyg.locateOnScreen(imgPath)
        xAxis = int (img[0] + (img[2] / 2))
        yAxis = int (img[1] + (img[3] / 2))
        pyg.click(xAxis, yAxis)
    except pyg.ImageNotFoundException:
        pass
        
        
        
        
def searchingPage (theLink):
    clickingArea("OpenPage.png")
    time.sleep(3)
    clickingArea("ExitPage.png")
    pyg.typewrite(theLink)
    time.sleep(1)
    pyg.hotkey("Enter")
    

def main():
    time.sleep(5)
    pyg.FAILSAFE = False
    clickingArea("TopLeft.png")
    time.sleep(1)
    clickingArea("FireFox.png")
    time.sleep(10)
    
    
    #Proton:
    searchingPage("https://account.proton.me/login")
    time.sleep(15)
    pyg.hotkey("Enter")
    time.sleep(20)
    clickingArea("ProtonMail.png")
    time.sleep(15)
    clickingArea("SelectAll.png")
    time.sleep(1)
    pyg.hotkey("t")
    
    #Gmail:
    searchingPage("https://www.google.com/")
    time.sleep(20)
    clickingArea("GLogin.png")
    time.sleep(5)
    pyg.typewrite("bdarwin@acad.ifma.edu.br")
    time.sleep(3)
    pyg.hotkey("Enter")
    time.sleep(3)
    pyg.hotkey("Enter")
    time.sleep(5)
    clickingArea("EnterGmail.png")
    time.sleep(45)
    clickingArea("SelectAllGml.png")
    time.sleep(10)
    clickingArea("RubIcon.png")
    time.sleep(10)

    #Gpt:
    searchingPage("https://chatgpt.com/?oai-dm=1")
    time.sleep(10)
    clickingArea("LogGpt.png")
    clickingArea("LogGpt.png")
    time.sleep(5)
    pyg.typewrite("brndarwin@proton.me")
    time.sleep(1)
    pyg.hotkey("Enter")
    time.sleep(5)
    pyg.hotkey("Enter")
    time.sleep(10)
    clickingArea("Profile.png")
    time.sleep(2)
    clickingArea("Settings.png")
    time.sleep(2)
    clickingArea("DeleteAll.png")
    time.sleep(2)
    clickingArea("ConfirmDelection.png")
    '''
    Stopped Here
    #Outlook:
    searchingPage("https://outlook.live.com/mail/0/")
    time.sleep(10)
    clickingArea("SignIn.png")
    time.sleep(5)
    for i in range (0,3):
        pyg.hotkey("Enter")
        time.sleep(3)
    '''

main()
