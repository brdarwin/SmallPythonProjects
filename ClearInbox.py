import pyautogui as pyg
import time
import os


def checkImage(imgPath, op):
    for i in range (0, 9):
        try:
            img  = pyg.locateOnScreen(imgPath)
            if op == 0:
                pyg.hotkey("Enter")
            elif op == 1:
                xAxis = int (img[0] + (img[2] / 2))
                yAxis = int (img[1] + (img[3] / 2))
                pyg.click(xAxis, yAxis)
            else:
                pass
            break
        except pyg.ImageNotFoundException:
            time.sleep(5)
    time.sleep(3)

def searchingPage(theLink):
    checkImage("OpenPage.png", 1)
    time.sleep(3)
    checkImage("ExitPage.png", 1)
    pyg.typewrite(theLink)
    time.sleep(1)
    pyg.hotkey("Enter")

def main():
    time.sleep(5)
    pyg.FAILSAFE = False
    checkImage("TopLeft.png", 1)
    time.sleep(1)
    checkImage("FireFox.png", 1)
    
    
    #Proton:
    searchingPage("https://account.proton.me/login")
    checkImage("ProtonEnter.png", 0)
    checkImage("ProtonMail.png", 1)
    checkImage("SelectAll.png", 1)
    pyg.hotkey("t")
    
    
    #Gmail:
    searchingPage("https://www.google.com/")
    checkImage("GLogin.png", 1)
    pyg.typewrite("bdarwin@acad.ifma.edu.br")
    checkImage("EnterGoo.png", 0)
    checkImage("EnterGoo.png", 0)
    checkImage("EnterGmail.png", 1)
    checkImage("SelectAllGml.png", 1)
    checkImage("RubIcon.png", 1)

    
    #Gpt:
    searchingPage("https://chatgpt.com/?oai-dm=1")
    checkImage("LogGpt.png", 1)
    checkImage("EnterGpt.png", 2)
    pyg.typewrite("brndarwin@proton.me")
    time.sleep(1)
    pyg.hotkey("Enter")
    checkImage("EnterPass.png", 0)
    checkImage("Profile.png", 1)
    checkImage("Settings.png", 1)
    checkImage("DeleteAll.png", 1)
    checkImage("ConfirmDelection.png", 1)
    
    
    #Outlook:
    searchingPage("https://outlook.live.com/mail/0/")
    checkImage("SignIn.png", 1)
    checkImage("Next.png", 0)
    checkImage("EnterOutlook.png", 0)
    checkImage("Yes.png", 0)  
    checkImage("Select.png", 1) 
    checkImage("SelectAllOut.png", 1)
    pyg.hotkey("Delete")
    checkImage("Yep.png", 1)
    
    

main()
