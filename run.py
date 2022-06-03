# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

def choose_player_name():
    """
    Player chooses witch or wizard name
    """
    player_name = input("Choose your witch or wizard name:\n ")
    print(f"Welcome, {player_name}!")


choose_player_name()
