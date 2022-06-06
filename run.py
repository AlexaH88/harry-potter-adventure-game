"""
Runs the game
"""


import time
import sys
import random
from collectibles import inventory
from collectibles import Wand
from collectibles import Pet
from questions import YesNo
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


def game_intro():
    """
    Runs game intro text
    """
    print("\n")

    slowprint(
        "Welcome to the Harry Potter Adventure Game!"
        + emoji_choices.lightning_emoji()
    )

    slowprint(
        "Strange things have been happening at Hogwarts lately..."
        + emoji_choices.castle_emoji()
    )

    slowprint(
        "And no one seems to be able to work out how to stop them..."
        + emoji_choices.surprised_emoji()
    )

    slowprint(
        "Could you be the witch or wizard we've been looking for?"
        + emoji_choices.wizard_emoji()
    )

    slowprint(
        "Please help, the Wizarding World needs you!"
        + emoji_choices.world_emoji()
    )


def choose_play_game():
    """
    Asks the user if they want to play the game or not
    """
    new_line()

    play_game_responses = YesNo(
        "Great choice, let the adventure begin!",
        "That's a shame, maybe next time!"
        )

    play_game_input = input("Ready to face up to the challenge? (y/n) \n")

    print("\n")

    if play_game_input == "y":
        slowprint(
            play_game_responses.yes_response()
            + emoji_choices.happy_emoji()
        )
    elif play_game_input == "n":
        slowprint(
            play_game_responses.no_response()
            + emoji_choices.sad_emoji()
        )
        exit_game()
    else:
        slowprint(
            play_game_responses.other_response()
            + emoji_choices.neutral_emoji()
        )
        choose_play_game()


def choose_game_instructions():
    """
    Asks the player if they want to read the game instructions or not
    """
    new_line()

    game_instructions_responses = YesNo(
        "Right, let me explain the game to you!",
        "Ok, let's carry on with the quest!"
        )

    game_instructions_input = input(
        "Would you like to hear the game instructions first? (y/n) \n"
        )

    print("\n")

    if game_instructions_input == "y":
        slowprint(
            game_instructions_responses.yes_response()
            + emoji_choices.happy_emoji()
        )
        game_instructions()
    elif game_instructions_input == "n":
        slowprint(
            game_instructions_responses.no_response()
            + emoji_choices.happy_emoji()
        )
        main_two()
    else:
        slowprint(
            game_instructions_responses.other_response()
            + emoji_choices.neutral_emoji()
        )
        choose_game_instructions()


def game_instructions():
    """
    Prints game instructions
    """
    new_line()

    slowprint(
        "The aim of the game is to find your way through Hogwarts."
        + emoji_choices.castle_emoji()
    )

    slowprint(
        "And to stop the dark magic that has been happening here recently..."
        + emoji_choices.darkmoon_emoji()
    )

    slowprint(
        "You must collect 5 items, by answering 5 questions correctly."
        + emoji_choices.question_emoji()
    )

    slowprint(
        "These will be asked by friendly faces that you encounter as you go."
        + emoji_choices.hug_emoji()
    )

    slowprint(
        "Each item will allow you to unlock the next room."
        + emoji_choices.door_emoji()
    )

    slowprint(
        "Here you will find the next item."
        + emoji_choices.magicball_emoji()
    )

    slowprint(
        "In the final room you will discover who is behind the malevolence."
        + emoji_choices.evil_emoji()
    )

    slowprint(
        "You must beat them by casting 3 spells in the correct order..."
        + emoji_choices.spell_emoji()
    )

    slowprint(
        "Good luck, we're counting on you!"
        + emoji_choices.luck_emoji()
    )

    main_two()


def choose_player_name():
    """
    Asks the player to choose their witch or wizard name
    """
    new_line()

    player_name_input = input("Choose your witch or wizard name: \n")

    print("\n")

    slowprint(
        f"Welcome, {player_name_input}!"
        + emoji_choices.wizard_emoji()
    )


def wand_backstory():
    """
    Prints backstory on Ollivander and player wand selection
    """
    new_line()

    slowprint(
        "Now, let's see. "
        "\U0001F914"
        "In order to save Hogwarts you're going to need a wand! "
        "\U0001F320"
        "Let's go and see our favourite wandmaker, Garrick Ollivander! "
        "\U0001F474"
        "'Welcome to my shop, you've come to the right place!' "
        "\U0001F3EC"
    )


def wand_request():
    """
    Asks the player to request a wand
    """
    new_line()

    wand_request_responses = YesNo(
        "'Lovely, let's see what we can find for you!'",
        "'Fine, but you won't get far without one!'"
        )

    wand_request_input = input(
        "'So, tell me, are you in need of a wand?' (y/n) \n"
        )

    print("\n")

    if wand_request_input == "y":
        slowprint(
            wand_request_responses.yes_response()
            + emoji_choices.happy_emoji()
            )
    elif wand_request_input == "n":
        slowprint(
            wand_request_responses.no_response()
            + emoji_choices.sad_emoji()
            )
        exit_game()
    else:
        slowprint(
            wand_request_responses.other_response()
            + emoji_choices.neutral_emoji())
        wand_request()


def assign_wand():
    """
    Randomly assigns the player one of three wand options,
    and adds it to the player's inventory
    """
    new_line()

    slowprint(
        "Ollivander looks you up and down, studying you carefully... "
        "\U0001F9D0"
    )

    wand_options = [
        "Harry Potter's wand",
        "Albus Dumbledore's wand",
        "Rubeus Hagrid's wand"]

    random_wand_options = random.choice(wand_options)

    slowprint(
        f"'{random_wand_options} will suit you nicely!' "
        "\U0001F320"
    )

    harry = Wand(
        "Harry Potter's wand",
        "11 inches",
        "holly",
        "Phoenix feather",
        "nice and supple",
        "\U0001F426")

    albus = Wand(
        "Albus Dumbledore's wand",
        "15 inches",
        "elder",
        "Thestral tail hair",
        "the most powerful wand ever to exist",
        "\U0001F31F")

    rubeus = Wand(
        "Rubeus Hagrid's wand",
        "16 inches",
        "oak",
        "unknown",
        "rather bendy",
        "\U0001F333")

    if "Harry Potter's wand" in random_wand_options:
        slowprint(harry.description())
        slowprint(harry.add_wand_to_inventory())
    elif "Albus Dumbledore's wand" in random_wand_options:
        slowprint(albus.description())
        slowprint(albus.add_wand_to_inventory())
    elif "Rubeus Hagrid's wand" in random_wand_options:
        slowprint(rubeus.description())
        slowprint(rubeus.add_wand_to_inventory())


def pet_backstory():
    """
    Prints backstory on The Magical Menagerie and player pet selection
    """
    new_line()

    slowprint(
        "Right, what's next? "
        "\U0001F914"
        "An animal companion to help you on your quest! "
        "\U0001F495"
        "Let's pop into The Magical Menagerie to get one! "
        "\U0001F3EC"
        "'Welcome to my shop, let me show you what lovely pets we've got!' "
        "\U0001F475"
    )


def pet_request():
    """
    Asks the player to choose one of four pet types,
    and adds it to the player's inventory
    """
    new_line()

    cat = Pet("cat", "climbing", "\U0001F431")
    rat = Pet("rat", "chewing", "\U0001F42D")
    toad = Pet("toad", "swimming", "\U0001F438")
    owl = Pet("owl", "flying", "\U0001F989")

    slowprint(
        "You can choose from the following: \n"
        "(a) cat \U0001F431 \n"
        "(b) rat \U0001F42D \n"
        "(c) toad \U0001F438 \n"
        "(d) owl \U0001F989 \n"
    )
    ask_for_pet = input("'Which pet would you like?' \n")

    print("\n")

    if "a" in ask_for_pet:
        slowprint(cat.choice_confirmation())
        slowprint(cat.description())
        slowprint(cat.add_pet_to_inventory())
    elif "b" in ask_for_pet:
        slowprint(rat.choice_confirmation())
        slowprint(rat.description())
        slowprint(rat.add_pet_to_inventory())
    elif "c" in ask_for_pet:
        slowprint(toad.choice_confirmation())
        slowprint(toad.description())
        slowprint(toad.add_pet_to_inventory())
    elif "d" in ask_for_pet:
        slowprint(owl.choice_confirmation())
        slowprint(owl.description())
        slowprint(owl.add_pet_to_inventory())
    else:
        slowprint(
            "Please enter a, b, c, or d. "
            "\U0001F610"
        )
        pet_request()


def travel_to_hogwarts_backstory():
    """
    Prints backstory on travelling to Hogwarts
    """
    new_line()

    slowprint(
        "So, now that that's done, let's get to it! "
        "Grab on to this portkey and let's go to Hogwarts! "
        "\U0001F3F0"
    )

    slowprint(
        "Here we are, I hope you're ready! "
        "Let's see now, how do we get inside? "
        "\U0001F914"
    )

    slowprint(
        "Ah, here's the entrance. "
        "OK, I can see here there are some instructions pinned to the door. "
        "\U0001F9D0"
    )


def first_door_challenge():
    """
    Prompts the player to solve the first challenge,
    in order to open the first door
    """
    new_line()

    slowprint(
        "The instructions read: "
        "You will need a key to unlock this door. "
        "\U0001F511")

    slowprint(
        "It's located in a chest in the Forbidden Forest. "
        "But there are several obstacles in the way: \n"
        "(a) A pond, perfect for swimming across... "
        "\U0001F4A7 \n"
        "(b) A big tree, perfect for climbing up... "
        "\U0001F332 \n"
        "(c) An ivy plant, perfect for chewing through... "
        "\U0001F33F \n"
        "(d) A small mountain, perfect for flying over... "
        "\U0001F5FB \n"
    )

    slowprint("Maybe your pet could help you here...")
    get_key = input("Which option do you pick? \n")

    print("\n")

    if "a" in get_key and "{'toad'}" in inventory:
        slowprint(
            "Yes, well done! "
            "Your toad will tackle that no problem! "
            "\U0001F438"
        )
    elif "b" in get_key and "{'cat'}" in inventory:
        slowprint(
            "Yes, well done! "
            "Your cat will tackle that no problem! "
            "\U0001F431"
        )
    elif "c" in get_key and "{'rat'}" in inventory:
        slowprint(
            "Yes, well done! "
            "Your rat will tackle that no problem! "
            "\U0001F42D"
        )
    elif "d" in get_key and "{'owl'}" in inventory:
        slowprint(
            "Yes, well done! "
            "Your owl will tackle that no problem! "
            "\U0001F989"
        )
    elif "a" in get_key and "{'toad'}" not in inventory:
        slowprint("Hmm no, your pet can't do that...")
        exit_game()
    elif "b" in get_key and "{'cat'}" not in inventory:
        slowprint("Hmm no, your pet can't do that...")
        exit_game()
    elif "c" in get_key and "{'rat'}" not in inventory:
        slowprint("Hmm no, your pet can't do that...")
        exit_game()
    elif "d" in get_key and "{'owl'}" not in inventory:
        slowprint("Hmm no, your pet can't do that...")
        exit_game()
    else:
        slowprint(
            "Please enter a, b, c, or d. "
            "\U0001F610"
        )
        first_door_challenge()


def request_inventory():
    """
    Allows the player to request viewing their inventory
    detailing all of their collected items
    """
    player_input = input(" ")
    if "i" in player_input:
        show_inventory()


def show_inventory():
    """
    Shows the player's inventory of collected items
    """
    print(inventory)


def request_exit_game():
    """
    Allows the player to request exiting the game
    """
    player_input = input(" ")
    if "e" in player_input:
        exit_game()


def exit_game():
    """
    Exits the game
    """
    slowprint("Game Over! \U0001F47E")
    sys.exit()


def main_one():
    """
    Runs first set of programme functions
    """
    game_intro()
    choose_play_game()
    choose_game_instructions()


def main_two():
    """
    Runs second set of programme functions
    """
    choose_player_name()
    wand_backstory()
    wand_request()
    assign_wand()
    pet_backstory()
    pet_request()
    travel_to_hogwarts_backstory()
    first_door_challenge()


main_one()
request_exit_game()
request_inventory()
