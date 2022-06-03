# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

def choose_play_game():
    """
    Asks the user if they want to play the game or not
    """
    play_game_options = input("Ready to face up to \
        the challenge? y/n \n").lower()
    if play_game_options == "y":
        play_game()
    elif play_game_options == "n":
        exit_game()
    else:
        print("Please choose either y or n, in lowercase.")


def choose_player_name():
    """
    Asks the user to choose their witch or wizard name
    """
    player_name = input("Choose your witch or wizard name: \n")
    print(f"Welcome, {player_name}!")


def main():
    """
    Run all programme functions
    """
    choose_player_name()
    choose_play_game()


main()
