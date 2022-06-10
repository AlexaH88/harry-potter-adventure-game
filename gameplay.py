"""
Contains classes for all the collectibles in the game
"""
import sys
import time
from emojis import Emoji


emoji_choices = Emoji()


# code taken from codegrepper.com and adapted - see README for details
def slowprint(all_strings):
    """
    Runs all text in the game on slow
    """
    for each_character in all_strings + "\n \n":
        sys.stdout.write(each_character)
        sys.stdout.flush()
        time.sleep(1./15)


def new_line():
    """
    Creates one new line, allowing for two new lines
    in between slowprint functions
    """
    print()


def exit_game():
    """
    Exits the game
    """
    slowprint(
        "Game Over!" +
        emoji_choices.gameover_emoji()
    )
    sys.exit()
