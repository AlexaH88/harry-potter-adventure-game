# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random
import sys


def game_intro():
    """
    Runs game intro text
    """
    print("Welcome to the Harry Potter Adventure Game!")
    print("\u26A1")
    print("Strange things have been happening at Hogwarts lately...")
    print("\U0001F3F0")
    print("And no one seems to be able to work out how to stop them...")
    print("Could you be the witch or wizard we've been looking for?")
    print("\U0001F9D9\u200D\u2642\uFE0F")
    print("Please help, the Wizarding World needs you!")
    print("\U0001F30D \n")


def choose_play_game():
    """
    Asks the user if they want to play the game or not
    """
    play_game_options = input("Ready to face up to the challenge? (y/n) \n")
    if play_game_options == "y":
        print("Great choice, let the adventure begin!")
        print("\U0001F642 \n")
    elif play_game_options == "n":
        print("That's a shame, maybe next time!")
        print("\U0001F641 \n")
        exit_game()
    else:
        print("Please choose either y or n.")
        print("\U0001F610 \n")
        choose_play_game()


def choose_player_name():
    """
    Asks the player to choose their witch or wizard name
    """
    player_name = input("Choose your witch or wizard name: \n")
    print(f"Welcome, {player_name}!")
    print("\U0001F9D9\u200D\u2642\uFE0F \n")


def wand_backstory():
    """
    Prints backstory on Ollivander and player wand selection
    """
    print("Now, first things first.")
    print("In order to save Hogwarts you're going to need a wand!")
    print("\U0001F320")
    print("Let's go and see our favourite wandmaker, Garrick Ollivander! \n")


def wand_request():
    """
    Asks the player to request a wand
    """
    ask_for_wand = input(
        "Ollivander: 'Welcome, are you in need of a wand?' (y/n) \n")
    if ask_for_wand == "y":
        print("Lovely, let's see what we can find for you!")
        print("\U0001F642 \n")
    elif ask_for_wand == "n":
        print("Fine, but you won't get far without one!")
        print("\U0001F641 \n")
        exit_game()
    else:
        print("Please choose either y or n.")
        print("\U0001F610 \n")
        wand_request()


def assign_wand():
    """
    Randomly assigns the player one of three wand options
    """
    print("Ollivander looks you up and down, studying you carefully... \n")

    wand_options = [
        "Harry Potter's wand",
        "Albus Dumbledore's wand",
        "Rubeus Hagrid's wand"]

    random_wand_options = random.choice(wand_options)

    print(f"{random_wand_options} will suit you nicely!")

    if "Harry Potter's Wand" in random_wand_options:
        print("This wand is 11 inches long,")
        print("is made with holly wood,")
        print("has a Phoenix feather core,")
        print("and is nice and supple.")
        print("\U0001F426 \n")
    elif "Albus Dumbledore's Wand" in random_wand_options:
        print("This wand is 15 inches long,")
        print("is made with elder wood,")
        print("has a Thestral tail hair core,")
        print("and is the most powerful wand ever to exist!")
        print("\U0001F31F \n")
    elif "Rubeus Hagrid's Wand" in random_wand_options:
        print("This wand is 16 inches long,")
        print("is made with oak wood,")
        print("has an unknown core,")
        print("and is rather bendy.")
        print("\U0001F333 \n")


def exit_game():
    """
    Exits the game
    """
    sys.exit()


def main():
    """
    Run all programme functions
    """
    game_intro()
    choose_play_game()
    choose_player_name()
    wand_backstory()
    wand_request()
    assign_wand()


main()
