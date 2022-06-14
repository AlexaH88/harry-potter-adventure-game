"""
Contains classes and functions for the gameplay in the game
"""
import sys
import time
from emojis import Emoji


emoji_choices = Emoji()


# general gameplay
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


def win_game():
    """
    Exits the game
    """
    slowprint(
        "Congratulations! You Win!" +
        emoji_choices.gamewin_emoji()
    )
    sys.exit()


# code related to all doors in the game
def door_backstory(number, location):
    """
    Runs backstory on each door
    """
    slowprint(
        f"Ah, here's the {number} door!" +
        emoji_choices.door_emoji()
    )

    slowprint(
        "I can see here there are some instructions pinned to it." +
        emoji_choices.monocle_emoji()
    )

    slowprint(
        "They read: 'You will need a key to unlock this door.'" +
        emoji_choices.key_emoji()
    )

    slowprint(
        f"It's located in a chest in {location}!" +
        emoji_choices.location_emoji()
    )


# code related to all rooms in the game
class Room():
    """
    Room class
    """
    def __init__(self, number, animal, person, pronoun_one, pronoun_two):
        """
        Creates an instance of Room
        """
        self.number = number
        self.animal = animal
        self.person = person
        self.pronoun_one = pronoun_one
        self.pronoun_two = pronoun_two

    def room_backstory(self):
        """
        Runs backstory on each room
        """
        slowprint(
            f"You enter the {self.number} room and look around..." +
            emoji_choices.door_emoji()
        )

        slowprint(
            f"Hang on, is that {self.animal}?!" +
            emoji_choices.animal_emoji()
        )

        slowprint(
            "That can only mean one thing..." +
            emoji_choices.lightbulb_emoji()
        )

        slowprint(
            f"It's {self.person}!" +
            emoji_choices.hug_emoji()
        )

        slowprint(
            f"Let's see if {self.pronoun_one} can help us." +
            emoji_choices.wizard_emoji()
        )

        new_line()

        slowprint(
            "'Look who we have here!'" +
            emoji_choices.monocle_emoji()
        )

        slowprint(
            f"'{self.pronoun_two} have something that could help you...'" +
            emoji_choices.magicball_emoji()
        )

        slowprint(
            "'But first you have to answer this question correctly!'" +
            emoji_choices.question_emoji()
        )
