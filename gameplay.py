"""
Contains classes and functions for the gameplay in the game
"""
import sys
import time
from emojis import Emoji


emoji_choices = Emoji()


# code taken from codegrepper.com and adapted - see README for details
def slowprint(all_strings):
    """
    Runs all strings in the game on slow
    """
    for each_character in all_strings + "\n":
        sys.stdout.write(each_character)
        sys.stdout.flush()
        time.sleep(1./15)


def exit_game():
    """
    Exits the game
    """
    slowprint(
        "Game Over!" +
        emoji_choices.gameover_emoji() +
        "Exiting game..." +
        emoji_choices.wave_emoji() +
        "To play again, click on the 'Run Game' button" +
        emoji_choices.videogame_emoji()
    )
    sys.exit()


def win_game():
    """
    Exits the game
    """
    slowprint(
        "Congratulations! You Win!" +
        emoji_choices.gamewin_emoji() +
        "Exiting game..." +
        emoji_choices.wave_emoji() +
        "To play again, click on the 'Run Game' button" +
        emoji_choices.videogame_emoji()
    )
    sys.exit()


def door_backstory(number, location):
    """
    Runs backstory on each door
    """
    slowprint(
        f"Ah, here's the {number} door!" +
        emoji_choices.door_emoji() +
        "I can see here there are some instructions pinned to it." +
        emoji_choices.monocle_emoji() +
        "They read: 'You will need a key to unlock this door.'" +
        emoji_choices.key_emoji() +
        f"It's located in a chest in {location}!" +
        emoji_choices.location_emoji()
    )


def room_backstory(number, animal, person, pronoun_one, pronoun_two):
    """
    Runs backstory on each room
    """
    slowprint(
            f"You enter the {number} room and look around..." +
            emoji_choices.door_emoji() +
            f"Hang on, is that {animal}?!" +
            emoji_choices.animal_emoji() +
            "That can only mean one thing..." +
            emoji_choices.lightbulb_emoji() +
            f"It's {person}!" +
            emoji_choices.hug_emoji() +
            f"Let's see if {pronoun_one} can help us." +
            emoji_choices.wizard_emoji() +
            "'Look who we have here!'" +
            emoji_choices.monocle_emoji() +
            f"'{pronoun_two} have something that could help you...'" +
            emoji_choices.magicball_emoji() +
            "'But first you have to answer this question correctly!'" +
            emoji_choices.question_emoji()
        )
