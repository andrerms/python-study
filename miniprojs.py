# Description of the mini projects can be found at https://knightlab.northwestern.edu/2014/06/05/five-mini-programming-projects-for-the-python-beginner/

from os import system # Import only system from OS
import random

options = [
            [1, "Dice Rolling Simulator", True],
            [2, "Guess the Number", True],
            [3, "Mad Libs Generator", True],
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
        guessNumber()
    elif choiceNumber == 3:
        madLibs()
    elif choiceNumber == 4:
        pass
    elif choiceNumber == 5:
        pass

    if choiceNumber == 6:
        mainMenu(False)
    else:
        mainMenu(True)


def guessNumber():
    playAgain = True

    while playAgain:
        cls()
        rnd = random.randrange(0, 101)

        print("WELCOME TO GUESS THE NUMBER!")
        print("Can you guess the number I have in my mind? (0 - 100)")
        userGuess = input()

        while str(userGuess) != str(rnd):
            if is_int(userGuess) == False:
                print("Numbers only! Try again...")
            elif int(userGuess) > rnd:
                print("Wrong answer! Think about a smaller number...")
            else:
                print("Wrong answer! Think about a bigger number...")

            userGuess = input()

        print("Congratulations! Number " + str(rnd) + " was my choice!")
        print("Wanna play again? (Y/N)")
        playAgain = input()
        if str(playAgain).upper() == "Y":
            playAgain = True
        else:
            playAgain = False

def madLibs():
    playAgain = True

    while playAgain:
        cls()
        verb1 = ""
        verb2 = ""
        verb3 = ""
        templateText = "Harry {0} into the air and the Firebolt {1} higher and faster than any other broom; he {2} around the stadium and began squinting around for the Snitch, listening all the while to the commentary, wich was being provided by the Weasley twins' friend Lee Jordan. (Harry Porter and the Prisoner of Azkaban, J.K. Rowling)" #http://nicole-singer.blogspot.com/2012/06/literary-mad-libs.html

        print("WELCOME TO MAD LIBS GENERATOR!")
        print("Please, give me a verb...")
        verb1 = input()
        print("Hum... Another verb, please...")
        verb2 = input()
        print("And guess what? One last verb. I promisse!")
        verb3 = input()

        print(templateText.format(verb1, verb2, verb3))
        print("Wanna play again? (Y/N)")
        playAgain = input()
        if str(playAgain).upper() == "Y":
            playAgain = True
        else:
            playAgain = False

mainMenu(True)
