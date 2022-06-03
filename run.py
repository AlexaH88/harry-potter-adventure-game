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
    print("Strange things have been happening at Hogwarts School of Witchcraft \
        and Wizardry...")
    print("And no one seems to be able to work out how to stop them...")
    print("Could you be the witch or wizard we've been looking for?")
    print("Please help, the Wizarding World needs you!")


def choose_play_game():
    """
    Asks the user if they want to play the game or not
    """
    play_game_options = input("Ready to face up to the challenge? (y/n) \n")
    if play_game_options == "y":
        print("Great choice, let the adventure begin!")
    elif play_game_options == "n":
        print("That's a shame, maybe next time!")
        exit_game()
    else:
        print("Please choose either y or n.")
        choose_play_game()


def choose_player_name():
    """
    Asks the player to choose their witch or wizard name
    """
    player_name = input("Choose your witch or wizard name: \n")
    print(f"Welcome, {player_name}!")


def wand_backstory():
    """
    Prints backstory on Ollivander and player wand selection
    """
    print("Now, first things first.")
    print("In order to beat Voldemort you're going to need a wand!")
    print("So, let's ask our favourite wandmaker, \
        Garrick Ollivander to assign you one!")


def assign_wand():
    """
    Randomly assigns the player one of three wand options
    """
    wand_options = [
        "Harry Potter's Wand",
        "Albus Dumbledore's Wand",
        "Rubeus Hagrid's Wand"]

    random_wand_options = random.choice(wand_options)

    print("Ollivander looks you up and down, studying you carefully.")
    print(f"{random_wand_options} will suit you nicely!")
    #print(f"{player_name}, {wand_options} will suit you nicely!")

    if "Harry Potter's Wand" in random_wand_options:
        print(f"{wand_options[0]} is 11 inches long, made with holly wood, \
            has a Phoenix feather core, and is nice and supple.")
    elif "Albus Dumbledore's Wand" in random_wand_options:
        print(f"{wand_options[1]} is 15 inches long, made with elder wood, \
            has a Thestral tail hair core, and is the most powerful wand ever \
            to exist!")
    elif "Rubeus Hagrid's Wand" in random_wand_options:
        print(f"{wand_options[2]} is 16 inches long, made with oak wood, \
            has an unknown core, and is rather bendy.")


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
    assign_wand()


main()
