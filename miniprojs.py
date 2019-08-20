# Description of the mini projects can be found at https://knightlab.northwestern.edu/2014/06/05/five-mini-programming-projects-for-the-python-beginner/

from os import system # Import only system from OS
import random

options = [
            [1, "Dice Rolling Simulator", True],
            [2, "Guess the Number", False],
            [3, "Mad Libs Generator", False],
            [4, "TextBased Adventure Game", False],
            [5, "Hangman", False],
            [6, "Exit the program", True]
          ]
choiceMsg = "Choose your game:"

def menu():
    cls()
    print("******************************************************")
    print("Five mini programming projects for the Python beginner")
    print("******************************************************")
    print("Available games:")
    for item in options:
        print(str(item[0]) + ".", item[1])
    print("******************************************************")
    global choiceMsg
    print(choiceMsg)
    choice = input()
    return choice

def diceRoll():
    cls()
    print("WELCOME TO DICE ROLLING SIMULATOR!")
    print("How many dice do you want to roll?")
    dice = input()

    if is_int(dice):
        dice = int(dice)
        i = 0
        while i < dice:
            i+=1
            rnd = random.randrange(1, 7)
            print("Dice", str(i) + ":", str(rnd))
        return footer()
    else:
        return "Y"

def footer():
        print("Try another time? (Y/N)")
        return input()

# Check if value is an integer
def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

# Execute cls system command
def cls():
    system("cls")

def mainMenu(showMenu):
    global choiceMsg

    # Show the menu while a valid option is not selected
    while showMenu == True:
        choiceNumber = menu()
        # Check if the option is valid
        if is_int(choiceNumber):
            choiceNumber = int(choiceNumber)
            if choiceNumber <= len(options):
                showMenu = not options[choiceNumber-1][2]
                if showMenu == True:
                    choiceMsg = "Game number " + str(choiceNumber) + " is not available yet - Choose your game:"
                else:
                    showGame(choiceNumber)
            else:
                choiceMsg = "Option " + str(choiceNumber) + " is not valid. Choose your game:"
        else:
            choiceMsg = "Option " + str(choiceNumber) + " is not valid. Choose your game:"

def showGame(choiceNumber):
    if choiceNumber == 1:
        go = "Y"
        while go == "Y":
            go = str(diceRoll()).upper()
    elif choiceNumber == 2:
        pass
    elif choiceNumber == 3:
        pass
    elif choiceNumber == 4:
        pass
    elif choiceNumber == 5:
        pass

    if choiceNumber == 6:
        mainMenu(False)
    else:
        mainMenu(True)

mainMenu(True)
