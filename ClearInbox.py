import pyautogui as pyg
import time
import os


def checkImage(imgPath, op):
    for i in range (0, 60):
        try:
            img  = pyg.locateOnScreen(imgPath)
            if op == 0:
                pyg.hotkey("Enter")
            elif op == 1:
                pyg.click(img)
            else:
                pass
            break
        except pyg.ImageNotFoundException:
            time.sleep(1)
    

def searchingPage(theLink):
    checkImage("OpenPage.png", 1)
    checkImage("ExitPage.png", 1)
    pyg.typewrite(theLink, interval=0.2)
    time.sleep(1)
    pyg.hotkey("Enter")

def main():
    screenSize = pyg.size()
    pyg.FAILSAFE = False
    checkImage("TopLeft.png", 1)
    checkImage("FireFox.png", 1)
    
    
    #Proton:
    searchingPage("https://account.proton.me/login")
    checkImage("ProtonEnter.png", 0)
    checkImage("ProtonMail.png", 1)
    checkImage("SelectAll.png", 1)
    pyg.hotkey("t")
    checkImage("EmptyProton.png", 2)
    
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
    checkImage("EmptyGpt.png", 2)
    
    #Outlook:
    searchingPage("https://outlook.live.com/mail/0/")
    checkImage("SignIn.png", 1)
    checkImage("Next.png", 0)
    checkImage("EnterOutlook.png", 0)
    checkImage("Yes.png", 0)  
    checkImage("Select.png", 1) 
    checkImage("SelectAllOut.png", 1)
    pyg.hotkey("Delete")
    time.sleep(3)
    pyg.hotkey("Enter")
    checkImage("EmptyOutlook.png", 2)

    
     #Gmail:
    searchingPage("https://www.google.com/")
    time.sleep(7)
    pyg.click(1279, 177)
    checkImage("bmail.png", 1)
    checkImage("EnterGoo.png", 0)
    checkImage("EnterGoo2.png", 0)
    checkImage("EnterGmail.png", 1)
    checkImage("SelectAllGml.png", 1)
    checkImage("RubIcon.png", 1)
    checkImage("EmptyGmail.png", 2)
    
    pyg.hotkey('Ctrl','q')
    print("Done")

main()
