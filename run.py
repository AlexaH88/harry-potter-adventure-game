"""
Runs the game
"""


import random
from collectibles import inventory, Wand, Pet, key_main, add_to_inventory
from questions import YesNo, AbcdOther, AbcdChallenge, AbcdQuestion
from gameplay import slowprint, new_line, exit_game, Room
from emojis import Emoji


emoji_choices = Emoji()
abcd_other_responses = AbcdOther()


# Functions that run the game story, in order

def game_intro():
    """
    Runs game intro text
    """
    new_line()

    slowprint(
        "Welcome to the Harry Potter Adventure Game!" +
        emoji_choices.lightning_emoji()
    )

    slowprint(
        "Strange things have been happening at Hogwarts lately..." +
        emoji_choices.castle_emoji()
    )

    slowprint(
        "And no one seems to be able to work out how to stop them..." +
        emoji_choices.surprised_emoji()
    )

    slowprint(
        "Could you be the witch or wizard we've been looking for?" +
        emoji_choices.wizard_emoji()
    )

    slowprint(
        "Please help, the Wizarding World needs you!" +
        emoji_choices.world_emoji()
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
            play_game_responses.yes_response() +
            emoji_choices.happy_emoji()
        )
    elif play_game_input == "n":
        slowprint(
            play_game_responses.no_response() +
            emoji_choices.sad_emoji()
        )
        exit_game()
    else:
        slowprint(
            play_game_responses.other_response() +
            emoji_choices.neutral_emoji()
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
            game_instructions_responses.yes_response() +
            emoji_choices.happy_emoji()
        )
        game_instructions()
    elif game_instructions_input == "n":
        slowprint(
            game_instructions_responses.no_response() +
            emoji_choices.happy_emoji()
        )
        main_two()
    else:
        slowprint(
            game_instructions_responses.other_response() +
            emoji_choices.neutral_emoji()
        )
        choose_game_instructions()


def game_instructions():
    """
    Runs game instructions
    """
    new_line()

    slowprint(
        "The aim of the game is to find your way through Hogwarts." +
        emoji_choices.castle_emoji()
    )

    slowprint(
        "And to stop the dark magic that has been happening here recently..." +
        emoji_choices.darkmoon_emoji()
    )

    slowprint(
        "You must collect 5 items, by answering 5 questions correctly." +
        emoji_choices.question_emoji()
    )

    slowprint(
        "These will be asked by friendly faces that you encounter as you go." +
        emoji_choices.hug_emoji()
    )

    slowprint(
        "Each item will allow you to unlock the next room." +
        emoji_choices.door_emoji()
    )

    slowprint(
        "Here you will find the next item." +
        emoji_choices.magicball_emoji()
    )

    slowprint(
        "In the final room you will discover who is behind the malevolence." +
        emoji_choices.evil_emoji()
    )

    slowprint(
        "You must beat them by casting 3 spells in the correct order..." +
        emoji_choices.spell_emoji()
    )

    slowprint(
        "Good luck, we're counting on you!" +
        emoji_choices.luck_emoji()
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
        f"Welcome, {player_name_input}!" +
        emoji_choices.wizard_emoji()
    )


def wand_backstory():
    """
    Runs backstory on Ollivander and player wand selection
    """
    new_line()

    slowprint(
        "Now, let's see." +
        emoji_choices.thinking_emoji()
    )

    slowprint(
        "In order to save Hogwarts, you're going to need a wand!" +
        emoji_choices.spell_emoji()
    )

    slowprint(
        "Let's go and see our favourite wandmaker, Garrick Ollivander!" +
        emoji_choices.oldman_emoji()
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

    slowprint(
        "'Welcome to my shop, you've come to the right place!'" +
        emoji_choices.shop_emoji()
    )

    wand_request_input = input(
        "'So, tell me, are you in need of a wand?' (y/n) \n"
        )

    print("\n")

    if wand_request_input == "y":
        slowprint(
            wand_request_responses.yes_response() +
            emoji_choices.happy_emoji()
            )
    elif wand_request_input == "n":
        slowprint(
            wand_request_responses.no_response() +
            emoji_choices.sad_emoji()
            )
        exit_game()
    else:
        slowprint(
            wand_request_responses.other_response() +
            emoji_choices.neutral_emoji())
        wand_request()


def assign_wand():
    """
    Randomly assigns the player one of three wand options,
    and adds it to the player's inventory
    """
    new_line()

    slowprint(
        "Ollivander looks you up and down, studying you carefully..." +
        emoji_choices.monocle_emoji()
    )

    wand_options = [
        "Harry Potter's wand",
        "Albus Dumbledore's wand",
        "Rubeus Hagrid's wand"]

    random_wand_options = random.choice(wand_options)

    slowprint(
        f"'{random_wand_options} will suit you nicely!'" +
        emoji_choices.spell_emoji()
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
        slowprint(
            harry.description() +
            emoji_choices.harrywand_emoji()
        )
        slowprint(
            harry.add_wand_to_inventory() +
            emoji_choices.backpack_emoji()
        )
    elif "Albus Dumbledore's wand" in random_wand_options:
        slowprint(
            albus.description() +
            emoji_choices.albuswand_emoji()
        )
        slowprint(
            albus.add_wand_to_inventory() +
            emoji_choices.backpack_emoji()
        )
    elif "Rubeus Hagrid's wand" in random_wand_options:
        slowprint(
            rubeus.description() +
            emoji_choices.rubeuswand_emoji()
        )
        slowprint(
            rubeus.add_wand_to_inventory() +
            emoji_choices.backpack_emoji()
        )


def pet_backstory():
    """
    Runs backstory on The Magical Menagerie and player pet selection
    """
    new_line()

    slowprint(
        "Right, what's next?" +
        emoji_choices.thinking_emoji()
    )

    slowprint(
        "An animal companion to help you on your quest!" +
        emoji_choices.animal_emoji()
    )

    slowprint(
        "Let's pop into The Magical Menagerie to get one!" +
        emoji_choices.shop_emoji()
    )


def pet_request():
    """
    Asks the player to choose one of four pet types,
    and adds it to the player's inventory
    """
    new_line()

    cat = Pet("cat", "climbing")
    rat = Pet("rat", "chewing")
    toad = Pet("toad", "swimming")
    owl = Pet("owl", "flying")

    slowprint(
        "'Welcome to my shop, let me show you what lovely pets we've got!'" +
        emoji_choices.oldlady_emoji()
    )

    slowprint(
        "You can choose from the following: \n"
        "(a) cat \U0001F431 \n"
        "(b) rat \U0001F42D \n"
        "(c) toad \U0001F438 \n"
        "(d) owl \U0001F989"
    )

    ask_for_pet = input("'Which pet would you like?' \n")

    print("\n")

    if "a" in ask_for_pet:
        slowprint(
            cat.choice_confirmation() +
            emoji_choices.cat_emoji()
        )
        slowprint(
            cat.description() +
            emoji_choices.animal_emoji()
        )
        slowprint(
            cat.add_pet_to_inventory() +
            emoji_choices.backpack_emoji()
        )
    elif "b" in ask_for_pet:
        slowprint(
            rat.choice_confirmation() +
            emoji_choices.rat_emoji()
        )
        slowprint(
            rat.description() +
            emoji_choices.animal_emoji()
        )
        slowprint(
            rat.add_pet_to_inventory() +
            emoji_choices.backpack_emoji()
        )
    elif "c" in ask_for_pet:
        slowprint(
            toad.choice_confirmation() +
            emoji_choices.toad_emoji()
        )
        slowprint(
            toad.description() +
            emoji_choices.animal_emoji()
        )
        slowprint(
            toad.add_pet_to_inventory() +
            emoji_choices.backpack_emoji()
        )
    elif "d" in ask_for_pet:
        slowprint(
            owl.choice_confirmation() +
            emoji_choices.owl_emoji()
        )
        slowprint(
            owl.description() +
            emoji_choices.animal_emoji()
        )
        slowprint(
            owl.add_pet_to_inventory() +
            emoji_choices.backpack_emoji()
        )
    else:
        slowprint(
            abcd_other_responses.other_response() +
            emoji_choices.neutral_emoji()
        )
        pet_request()


def travel_to_hogwarts_backstory():
    """
    Runs backstory on travelling to Hogwarts
    """
    new_line()

    slowprint(
        "So, now that that's done, let's get to it!" +
        emoji_choices.lightning_emoji()
    )

    slowprint(
        "Grab on to this portkey and let's go to Hogwarts!" +
        emoji_choices.castle_emoji()
    )

    slowprint(
        "Here we are, I hope you're ready!" +
        emoji_choices.luck_emoji()
    )

    slowprint(
        "Let's see now, how do we get inside?" +
        emoji_choices.thinking_emoji()
    )

    slowprint(
        "Ah, here's the entrance!" +
        emoji_choices.door_emoji()
    )

    slowprint(
        "OK, I can see here there are some instructions pinned to the door." +
        emoji_choices.monocle_emoji()
    )


def first_key_challenge():
    """
    Prompts the player to solve the first key challenge,
    in order to open the first door
    """
    new_line()

    first_door_choices = AbcdChallenge(
        "Yes, well done! Your toad will tackle that no problem!",
        "Yes, well done! Your cat will tackle that no problem!",
        "Yes, well done! Your rat will tackle that no problem!",
        "Yes, well done! Your owl will tackle that no problem!",
        "Hmm no, your pet can't do that!"
    )

    slowprint(
        "The instructions read: 'You will need a key to unlock this door.'" +
        emoji_choices.key_emoji()
    )

    slowprint(
        "It's located in a chest in the Forbidden Forest." +
        emoji_choices.forest_emoji()
    )

    slowprint(
        "But there are several obstacles in the way: \n"
        "(a) A pond, perfect for swimming across... "
        "\U0001F4A7 \n"
        "(b) A big tree, perfect for climbing up... "
        "\U0001F332 \n"
        "(c) An ivy plant, perfect for chewing through... "
        "\U0001F33F \n"
        "(d) A small mountain, perfect for flying over... "
        "\U0001F5FB"
    )

    slowprint(
        "Maybe your pet could help you here..." +
        emoji_choices.animal_emoji()
        )
    first_door_input = input("Which option do you pick? \n")

    print("\n")

    if "a" in first_door_input and "{'toad'}" in inventory:
        slowprint(
            first_door_choices.a_response_correct() +
            emoji_choices.toad_emoji()
        )
        key_main()
    elif "b" in first_door_input and "{'cat'}" in inventory:
        slowprint(
            first_door_choices.b_response_correct() +
            emoji_choices.cat_emoji()
        )
        key_main()
    elif "c" in first_door_input and "{'rat'}" in inventory:
        slowprint(
            first_door_choices.c_response_correct() +
            emoji_choices.rat_emoji()
        )
        key_main()
    elif "d" in first_door_input and "{'owl'}" in inventory:
        slowprint(
            first_door_choices.d_response_correct() +
            emoji_choices.owl_emoji()
        )
        key_main()
    elif "a" in first_door_input and "{'toad'}" not in inventory:
        slowprint(
            first_door_choices.response_incorrect() +
            emoji_choices.animal_emoji()
        )
        exit_game()
    elif "b" in first_door_input and "{'cat'}" not in inventory:
        slowprint(
            first_door_choices.response_incorrect() +
            emoji_choices.animal_emoji()
        )
        exit_game()
    elif "c" in first_door_input and "{'rat'}" not in inventory:
        slowprint(
            first_door_choices.response_incorrect() +
            emoji_choices.animal_emoji()
        )
        exit_game()
    elif "d" in first_door_input and "{'owl'}" not in inventory:
        slowprint(
            first_door_choices.response_incorrect() +
            emoji_choices.animal_emoji()
        )
        exit_game()
    else:
        slowprint(
            abcd_other_responses.other_response() +
            emoji_choices.neutral_emoji()
        )
        first_key_challenge()


def first_room_backstory():
    """
    Runs first room backstory
    """
    new_line()

    first_room = Room(
        "first",
        "pygmy puff",
        "Fred and George Weasley",
        "they",
        "We"
        )

    slowprint(first_room.room_backstory())


def first_item_question():
    """
    Prompts the player to solve the first room question,
    in order to obtain an item required to open the
    next door
    """
    new_line()

    first_room_choices = AbcdQuestion(
        "'I see you're a fan! I think you'll like this item...'",
        "'Nope, that's from a different shop in Diagon Alley!'"
    )

    slowprint(
        "Out of the following items: \n"
        "(a) The Monster Book of Monsters. "
        "\U0001F4D6 \n"
        "(b) Dungbombs. "
        "\U0001F4A3 \n"
        "(c) Extendable Ears. "
        "\U0001F442 \n"
        "(d) Butterbeer. "
        "\U0001F37A"
    )

    first_room_input = input(
        "'Which item is available for sale at Weasleys' Wizard Wheezes?' \n"
        )

    print("\n")

    if "c" in first_room_input:
        slowprint(
            first_room_choices.response_correct() +
            emoji_choices.map_emoji()
        )
        add_to_inventory("Marauder's Map")
    elif "a" or "b" or "d" in first_room_input:
        slowprint(
            first_room_choices.response_incorrect() +
            emoji_choices.sad_emoji()
        )
        exit_game()
    else:
        slowprint(
            abcd_other_responses.other_response() +
            emoji_choices.neutral_emoji()
        )
        first_item_question()


# Call the functions from game story to allow it to run
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
    first_key_challenge()
    first_room_backstory()
    first_item_question()


main_one()
