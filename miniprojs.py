# https://knightlab.northwestern.edu/2014/06/05/five-mini-programming-projects-for-the-python-beginner/

# Import only system from OS
from os import system

showMenu = True
options = [
            [1, "Dice Rolling Simulator", True],
            [2, "Guess the Number", False],
            [3, "Mad Libs Generator", False],
            [4, "TextBased Adventure Game", False],
            [5, "Hangman", False]
          ]
choiceNumber = 0
choiceName = ""
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
    print(choiceMsg)
    choice = input()
    return choice

def diceRoll():
    cls()

# Execute cls system command
def cls():
    system("cls")

# Show the menu while a valid option is not selected
while showMenu == True:
    choiceNumber = int(menu())
    # Check if the option 
    if choiceNumber <= len(options):
        showMenu = not options[choiceNumber-1][2]
        choiceName = options[choiceNumber-1][1]
        if showMenu == True:
            choiceMsg = "Game number " + str(choiceNumber) + " is not available yet - Choose your game:"
    else:
        choiceMsg = "Option " + str(choiceNumber) + " is not valid. Choose your game:"
