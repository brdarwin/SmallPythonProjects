import re
import random
import sys

class Game ():

    def __init__(Self, numDigits, numAtempts):
        Self.numDigits = numDigits
        Self.numAtempts = numAtempts
        Self.atemptsLeft = Self.numAtempts
        minNum = 10 ** (Self.numDigits - 1)
        maxNum = (10 ** Self.numDigits) - 1
        Self.theNumber = str(random.randint(minNum,maxNum))

    def instructionsMenu (Self):
        print ("\n\nInstructions:")
        print ("You have {} attempt(s) to guess the {} digit(s) number.You'll receive clues, if you find some digit.".format(Self.numAtempts, Self.numDigits))
        print ("Digit 'help' for instructions.\nDigit 'restart' to restart the game.")
        print ("Digit 'edit' to change the game's standards.\nDigit 'quit' to exit the game.\n\n")

    def restartGame(Self):
        Self.atemptsLeft = Self.numAtempts
        print("game restarted")
        Self.instructionsMenu()

    def restartingAux(Self):
        minNum = 10 ** (Self.numDigits - 1)
        maxNum = (10 ** Self.numDigits) - 1
        Self.theNumber = str(random.randint(minNum,maxNum))
        Self.restartGame()

    def editGame(Self):
        newAtempts = 0
        newNum = 0
        try:
            newAtempts = int(input("The new number of atempts: "))
            newNum = int(input("The new number of digits: "))
            if newAtempts <= 0 or newNum <= 0:
              raise ValueError("You must use  only positive integers.")
        except ValueError as ve:
            invalidRegex = re.compile(r'invalid')
            foundIt = invalidRegex.search(str(ve))
            if foundIt != None:
                print("You must only use positive integers")
                Self.editGame()
            print(ve)
            Self.editGame()
        Self.numAtempts = newAtempts
        Self.numDigits = newNum
        print("Changes saved!")
        Self.restartingAux()

    def comparingNumbers(Self, possibleNum):
        if( Self.theNumber == possibleNum):
            op = input(("You got it! Do you want start a new game?(digit 'y' for 'yes' or 'n' for 'no'.): "))
            if (op == 'y'):
                Self.restartingAux()
            else:
                sys.exit()
        else:
            howManyDigits = 0
            for i in range (0, Self.numDigits):
                if Self.theNumber[i] == possibleNum[i]:
                    howManyDigits += 1
            if (howManyDigits > 0):
                print("You found {} digit(s) in the right position.".format(howManyDigits))
            else:
                numRegex = re.compile(r'['+Self.theNumber+']')
                option = len(numRegex.findall(possibleNum))
                if(option == 1):
                    print("You found 1 digit, but it isn't in right position.")
                elif(option > 1):
                    print("You found {} digits, but they aren't in the right position.".format(option))
                else:
                    print("wrong number.")
            Self.atemptsLeft -= 1

    def decisionsMenu(Self):
        if (Self.atemptsLeft < 1):
            op=(input("You lost, the right number is {}. Do you want  try again?(digit 'y' for 'yes' or 'n' for 'no')".format(Self.theNumber)))
            if (op == 'y'):
                Self.restartingAux()
            else:
                sys.exit()
        decisionVar = str(input("You have {} atempt(s) left,guess the {} digit(s) number: ".format(Self.atemptsLeft, Self.numDigits)))
        possibleRegex = re.compile(r'\d{'+ str(Self.numDigits) + '}')
        possibleNum = possibleRegex.search(decisionVar)
        if (decisionVar == "help"):
            Self.instructionsMenu()
            return True
        elif(decisionVar == "quit"):
            pass
        elif(decisionVar == "edit"):
            Self.editGame()
            return True
        elif(decisionVar =="restart"):
            Self.restartGame()
            return True
        elif(possibleNum != None):
            Self.comparingNumbers(possibleNum.group())
            return True
        else:
            print ("Invalid number or command.")
            return True
        return False

def main ():
    myGame = Game(3, 10)
    print ("Guess The Number Game.")
    myGame.instructionsMenu()
    myBool = bool(True)
    while (myBool == True):
        myBool = myGame.decisionsMenu()
    sys.exit()
    return 0

main()
