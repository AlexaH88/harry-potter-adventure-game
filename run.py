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
    print("\U0001F632")
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
    print("Now, let's see.")
    print("\U0001F914")
    print("In order to save Hogwarts you're going to need a wand!")
    print("\U0001F320")
    print("Let's go and see our favourite wandmaker, Garrick Ollivander!")
    print("\U0001F474 \n")
    print("'Welcome to my shop, you've come to the right place!'")
    print("\U0001F3EC")


def wand_request():
    """
    Asks the player to request a wand
    """
    ask_for_wand = input(
        "'So, tell me, are you in need of a wand?' (y/n) \n")

    if ask_for_wand == "y":
        print("'Lovely, let's see what we can find for you!'")
        print("\U0001F642 \n")
    elif ask_for_wand == "n":
        print("'Fine, but you won't get far without one!'")
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
    print("Ollivander looks you up and down, studying you carefully...")
    print("\U0001F9D0 \n")

    wand_options = [
        "Harry Potter's wand",
        "Albus Dumbledore's wand",
        "Rubeus Hagrid's wand"]

    random_wand_options = random.choice(wand_options)

    print(f"'{random_wand_options} will suit you nicely!'")
    print("\U0001F320 \n")

    if "Harry Potter's wand" in random_wand_options:
        print("'This wand is 11 inches long,'")
        print("'is made with holly wood,'")
        print("'has a Phoenix feather core,'")
        print("'and is nice and supple.'")
        print("\U0001F426 \n")
    elif "Albus Dumbledore's wand" in random_wand_options:
        print("'This wand is 15 inches long,'")
        print("'is made with elder wood,'")
        print("'has a Thestral tail hair core,'")
        print("'and is the most powerful wand ever to exist!'")
        print("\U0001F31F \n")
    elif "Rubeus Hagrid's wand" in random_wand_options:
        print("'This wand is 16 inches long,'")
        print("'is made with oak wood,'")
        print("'has an unknown core,'")
        print("'and is rather bendy.'")
        print("\U0001F333 \n")


def pet_backstory():
    """
    Prints backstory on The Magical Menagerie and player pet selection
    """
    print("Right, what's next?")
    print("\U0001F914 \n")
    print("An animal companion to help you on your quest!")
    print("\U0001F495 \n")
    print("Let's pop into The Magical Menagerie to get one!")
    print("\U0001F3EC \n")
    print("'Welcome to my shop, let me show you what lovely pets we've got!'")
    print("\U0001F431 \U0001F42D \U0001F438 \U0001F989 \n")


def pet_request():
    """
    Asks the player to choose one of four pet types
    """
    pet_types = [
        "cat",
        "rat",
        "toad",
        "owl"]

    print("You can choose from the following: ")
    print("a) cat")
    print("b) rat")
    print("c) toad")
    print("d) owl \n")

    ask_for_pet = input("'Which pet would you like? (a, b, c, d)' \n")

    if "a" in ask_for_pet:
        print(f"'Great choice! You'll love your {pet_types[0]}'")
        print(f"'{pet_types[0]}s are known for:'")
        print("'their impressive climbing skills'.")
        print("'Use this wisely!'")
        print("\U0001F431 \n")
    elif "b" in ask_for_pet:
        print(f"'Great choice! You'll love your {pet_types[1]}'")
        print(f"'{pet_types[1]}s are known for:'")
        print("'their impressive chewing skills.'")
        print("'Use this wisely!'")
        print("\U0001F42D \n")
    elif "c" in ask_for_pet:
        print(f"'Great choice! You'll love your {pet_types[2]}'")
        print(f"'{pet_types[2]}s are known for:'")
        print("'their impressive swimming skills.'")
        print("'Use this wisely!'")
        print("\U0001F438 \n")
    elif "d" in ask_for_pet:
        print(f"'Great choice! You'll love your {pet_types[3]}'")
        print(f"'{pet_types[3]}s are known for:'")
        print("'their impressive flying skills.'")
        print("'Use this wisely!'")
        print("\U0001F989 \n")
    else:
        print("Please enter a, b, c, or d.")
        print("\U0001F610 \n")
        pet_request()


def exit_game():
    """
    Exits the game
    """
    sys.exit()


def main():
    """
    Runs all programme functions
    """
    game_intro()
    choose_play_game()
    choose_player_name()
    wand_backstory()
    wand_request()
    assign_wand()
    pet_backstory()
    pet_request()


main()
