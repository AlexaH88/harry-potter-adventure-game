# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random


def choose_play_game():
    """
    Asks the user if they want to play the game or not
    """
    play_game_options = input("Ready to face up to the challenge? (y/n) \n")
    if play_game_options == "y":
        #play_game()
        print("Play game")
    elif play_game_options == "n":
        #exit_game()
        print("Exit game")
    else:
        print("Please choose either y or n.")


def choose_player_name():
    """
    Asks the player to choose their witch or wizard name
    """
    player_name = input("Choose your witch or wizard name: \n")
    print(f"Welcome, {player_name}!")


def assign_wand():
    """
    Assigns the player one of three wand options
    """
    wand_options = random.choice([
        "Harry Potter's Wand",
        "James Potter's Wand",
        "Lily Potter's Wand"])
    print("Garrick Ollivander looks you up and down, studying you carefully.")
    print(f"Test, {wand_options} will suit you nicely!")
    #print(f"{player_name}, {wand_options} will suit you nicely!")


#def play_game():
#"""
#Starts the game
#"""


#def exit_game():
#"""
#Exits the game
#"""


def main():
    """
    Run all programme functions
    """
    choose_player_name()
    choose_play_game()
    assign_wand()
    #play_game()
    #exit_game()


main()
