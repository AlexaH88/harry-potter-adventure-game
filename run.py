"""
Runs the game
"""

import sys
import random
from collectibles import inventory
from collectibles import Wand
from collectibles import Pet
from questions import YesNo


def game_intro():
    """
    Runs game intro text
    """
    print(
        "\n"
        "Welcome to the Harry Potter Adventure Game! "
        "\u26A1 \n \n"
        "Strange things have been happening at Hogwarts lately... "
        "\U0001F3F0 \n"
        "And no one seems to be able to work out how to stop them... "
        "\U0001F632 \n \n"
        "Could you be the witch or wizard we've been looking for? "
        "\U0001F9D9\u200D\u2642\uFE0F \n"
        "Please help, the Wizarding World needs you! "
        "\U0001F30D \n"
    )


def choose_play_game():
    """
    Asks the user if they want to play the game or not
    """
    play_game_responses = YesNo(
        "Great choice, let the adventure begin!",
        "That's a shame, maybe next time!",
        "Please choose either y or n.",
        )

    play_game_input = input("Ready to face up to the challenge? (y/n) \n")

    if play_game_input == "y":
        print(play_game_responses.yes_response())
    elif play_game_input == "n":
        print(play_game_responses.no_response())
        exit_game()
    else:
        print(play_game_responses.other_response())
        choose_play_game()


def choose_game_instructions():
    """
    Asks the player if they want to read the game instructions or not
    """
    game_instructions_responses = YesNo(
        "Right, let me explain the game to you!",
        "Ok, let's carry on with the quest!",
        "Please choose either y or n.",
        )

    game_instructions_input = input(
        "Would you like to hear the game instructions first? (y/n) \n"
        )

    if game_instructions_input == "y":
        print(game_instructions_responses.yes_response())
        game_instructions()
    elif game_instructions_input == "n":
        print(game_instructions_responses.no_response())
        main_two()
    else:
        print(game_instructions_responses.other_response())
        choose_game_instructions()


def game_instructions():
    """
    Prints game instructions
    """
    print(
        "The aim of the game is to find your way through Hogwarts "
        "School of Witchcraft and Wizardry, and to stop the dark "
        "magic that has been happening here recently... "
        "\U0001F311 \n \n"

        "You must collect 5 items, by answering 5 questions correctly, "
        "asked by friendly faces that you encounter along the way. "
        "\U0001F917 \n \n"

        "Each item will allow you to unlock the next room, where you will "
        "find the next item. In the 5th and final room, you will discover "
        "who is behind the malevolence, and you must beat them by "
        "casting 3 spells in the correct order... "
        "\U0001F320 \n \n"

        "Good luck, we're counting on you! "
        "\U0001F340 \n"
    )

    main_two()


def choose_player_name():
    """
    Asks the player to choose their witch or wizard name
    """
    player_name_input = input("Choose your witch or wizard name: \n")

    print(
        f"\nWelcome, {player_name_input}! "
        "\U0001F9D9\u200D\u2642\uFE0F \n"
    )


def wand_backstory():
    """
    Prints backstory on Ollivander and player wand selection
    """
    print(
        "Now, let's see. "
        "\U0001F914 \n"
        "In order to save Hogwarts you're going to need a wand! "
        "\U0001F320 \n"
        "Let's go and see our favourite wandmaker, Garrick Ollivander! "
        "\U0001F474 \n \n"
        "'Welcome to my shop, you've come to the right place!' "
        "\U0001F3EC"
    )


def wand_request():
    """
    Asks the player to request a wand
    """
    wand_request_responses = YesNo(
        "'Lovely, let's see what we can find for you!'",
        "'Fine, but you won't get far without one!'",
        "Please choose either y or n.",
        )

    wand_request_input = input(
        "'So, tell me, are you in need of a wand?' (y/n) \n"
        )

    if wand_request_input == "y":
        print(wand_request_responses.yes_response())
    elif wand_request_input == "n":
        print(wand_request_responses.no_response())
        exit_game()
    else:
        print(wand_request_responses.other_response())
        wand_request()


def assign_wand():
    """
    Randomly assigns the player one of three wand options,
    and adds it to the player's inventory
    """
    print(
        "Ollivander looks you up and down, studying you carefully... "
        "\U0001F9D0 \n"
    )

    wand_options = [
        "Harry Potter's wand",
        "Albus Dumbledore's wand",
        "Rubeus Hagrid's wand"]

    random_wand_options = random.choice(wand_options)

    print(
        f"'{random_wand_options} will suit you nicely!' "
        "\U0001F320"
    )

    harry = Wand(
        "Harry Potter's wand",
        "11 inches",
        "holly",
        "Phoenix feather",
        "nice and supple")

    albus = Wand(
        "Albus Dumbledore's wand",
        "15 inches",
        "elder",
        "Thestral tail hair",
        "the most powerful wand ever to exist")

    rubeus = Wand(
        "Rubeus Hagrid's wand",
        "16 inches",
        "oak",
        "unknown",
        "rather bendy")

    if "Harry Potter's wand" in random_wand_options:
        print(harry.description() + "\U0001F426 \n")
        print(harry.add_wand_to_inventory() + "\U0001F392 \n")
    elif "Albus Dumbledore's wand" in random_wand_options:
        print(albus.description() + "\U0001F31F \n")
        print(albus.add_wand_to_inventory() + "\U0001F392 \n")
    elif "Rubeus Hagrid's wand" in random_wand_options:
        print(rubeus.description() + "\U0001F333 \n")
        print(rubeus.add_wand_to_inventory() + "\U0001F392 \n")


def pet_backstory():
    """
    Prints backstory on The Magical Menagerie and player pet selection
    """
    print(
        "Right, what's next? "
        "\U0001F914 \n"
        "An animal companion to help you on your quest! "
        "\U0001F495 \n"
        "Let's pop into The Magical Menagerie to get one! "
        "\U0001F3EC \n \n"
        "'Welcome to my shop, let me show you what lovely pets we've got!' "
        "\U0001F475 \n"
    )


def pet_request():
    """
    Asks the player to choose one of four pet types,
    and adds it to the player's inventory
    """
    cat = Pet("cat", "climbing", "\U0001F431")
    rat = Pet("rat", "chewing", "\U0001F42D")
    toad = Pet("toad", "swimming", "\U0001F438")
    owl = Pet("owl", "flying", "\U0001F989")

    print(
        "You can choose from the following: \n"
        "(a) cat \U0001F431 \n"
        "(b) rat \U0001F42D \n"
        "(c) toad \U0001F438 \n"
        "(d) owl \U0001F989 \n"
    )
    ask_for_pet = input("'Which pet would you like?' \n")

    if "a" in ask_for_pet:
        print(cat.choice_confirmation())
        print(cat.description())
        print(cat.add_pet_to_inventory())
    elif "b" in ask_for_pet:
        print(rat.choice_confirmation())
        print(rat.description())
        print(rat.add_pet_to_inventory())
    elif "c" in ask_for_pet:
        print(toad.choice_confirmation())
        print(toad.description())
        print(toad.add_pet_to_inventory())
    elif "d" in ask_for_pet:
        print(owl.choice_confirmation())
        print(owl.description())
        print(owl.add_pet_to_inventory())
    else:
        print(
            "\n"
            "Please enter a, b, c, or d. "
            "\U0001F610 \n"
        )
        pet_request()


def travel_to_hogwarts_backstory():
    """
    Prints backstory on travelling to Hogwarts
    """
    print(
        "So, now that that's done, let's get to it! "
        "Grab on to this portkey and let's go to Hogwarts! "
        "\U0001F3F0 \n"
    )

    print(
        "Here we are, I hope you're ready! "
        "Let's see now, how do we get inside? "
        "\U0001F914 \n"
    )

    print(
        "Ah, here's the entrance. "
        "OK, I can see here there are some instructions pinned to the door. "
        "\U0001F9D0 \n"
    )


def first_door_challenge():
    """
    Prompts the player to solve the first challenge,
    in order to open the first door
    """
    print(
        "The instructions read: "
        "You will need a key to unlock this door. "
        "\U0001F511 \n")

    print(
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

    print("Maybe your pet could help you here...")
    get_key = input("Which option do you pick? \n")

    if "a" in get_key and "{'toad'}" in inventory:
        print(
            "\n"
            "Yes, well done! "
            "Your toad will tackle that no problem! "
            "\U0001F438 \n"
        )
    elif "b" in get_key and "{'cat'}" in inventory:
        print(
            "\n"
            "Yes, well done! "
            "Your cat will tackle that no problem! "
            "\U0001F431 \n"
        )
    elif "c" in get_key and "{'rat'}" in inventory:
        print(
            "\n"
            "Yes, well done! "
            "Your rat will tackle that no problem! "
            "\U0001F42D \n"
        )
    elif "d" in get_key and "{'owl'}" in inventory:
        print(
            "\n"
            "Yes, well done! "
            "Your owl will tackle that no problem! "
            "\U0001F989 \n"
        )
    elif "a" in get_key and "{'toad'}" not in inventory:
        print("\n Hmm no, your pet can't do that... \n")
        exit_game()
    elif "b" in get_key and "{'cat'}" not in inventory:
        print("\n Hmm no, your pet can't do that... \n")
        exit_game()
    elif "c" in get_key and "{'rat'}" not in inventory:
        print("\n Hmm no, your pet can't do that... \n")
        exit_game()
    elif "d" in get_key and "{'owl'}" not in inventory:
        print("\n Hmm no, your pet can't do that... \n")
        exit_game()
    else:
        print(
            "\n"
            "Please enter a, b, c, or d. "
            "\U0001F610 \n"
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
    print("Game Over! \U0001F47E \n")
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
