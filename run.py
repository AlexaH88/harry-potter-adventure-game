"""
Runs the game
"""


# Imports modules
import random
from collectibles import inventory, Wand, Pet, key_main, add_to_inventory
from questions import YesNo, Abcd, AbcdOther, yes_no_response
from gameplay import (
    slowprint, new_line, exit_game, win_game, Room, door_backstory
    )
from emojis import Emoji


# Declares variables
emoji_choices = Emoji()
abcd_other_responses = AbcdOther()


# Prints game art, taken from textart.io - see README for details
print(r"""
                                          _ __
         ___                             | '  \
    ___  \ /  ___         ,'\_           | .-. \        /|
    \ /  | |,'__ \  ,'\_  |   \          | | | |      ,' |_   /|
  _ | |  | |\/  \ \ |   \ | |\_|    _    | |_| |   _ '-. .-',' |_   _
 // | |  | |____| | | |\_|| |__    //    |     | ,'_`. | | '-. .-',' `. ,'\_
 \\_| |_,' .-, _  | | |   | |\ \  //    .| |\_/ | / \ || |   | | / |\  \|   \
  `-. .-'| |/ / | | | |   | | \ \//     |  |    | | | || |   | | | |_\ || |\_|
    | |  | || \_| | | |   /_\  \ /      | |`    | | | || |   | | | .---'| |
    | |  | |\___,_\ /_\ _      //       | |     | \_/ || |   | | | |  /\| |
    /_\  | |           //_____//       .||`      `._,' | |   | | \ `-' /| |
         /_\           `------'        \ |              `.\  | |  `._,' /_\
                                        \|                    `.\
""")


# Functions that run the game story, in order

def game_intro():
    """
    Runs game intro text
    """
    slowprint(
        "Welcome to the Harry Potter Adventure Game!" +
        emoji_choices.lightning_emoji() +
        "Strange things have been happening at Hogwarts lately..." +
        emoji_choices.castle_emoji() +
        "And no one seems to be able to work out how to stop them..." +
        emoji_choices.surprised_emoji() +
        "Could you be the witch or wizard we've been looking for?" +
        emoji_choices.wizard_emoji() +
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
        "Would you like to read the game instructions first? (y/n) \n"
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
    slowprint(
        "The aim of the game is to find your way through Hogwarts." +
        emoji_choices.castle_emoji() +
        "And to stop the dark magic that has been happening here recently..." +
        emoji_choices.darkmoon_emoji() +
        "You must collect 3 items, by answering 3 questions correctly." +
        emoji_choices.question_emoji() +
        "These will be asked by friendly faces that you encounter as you go." +
        emoji_choices.hug_emoji() +
        "Each item will allow you to find a key to unlock the next room." +
        emoji_choices.door_emoji() +
        "Here you will find the next item." +
        emoji_choices.magicball_emoji() +
        "In the final room you will discover who is behind the malevolence." +
        emoji_choices.evil_emoji() +
        "You must beat them by choosing 2 spells correctly..." +
        emoji_choices.spell_emoji() +
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
    slowprint(
        "Now, let's see." +
        emoji_choices.thinking_emoji() +
        "In order to save Hogwarts, you're going to need a wand!" +
        emoji_choices.spell_emoji() +
        "Let's go and see our favourite wandmaker, Garrick Ollivander!" +
        emoji_choices.oldman_emoji()
    )


def wand_request():
    """
    Asks the player to request a wand
    """
    new_line()

    slowprint(
        "'Welcome to my shop, you've come to the right place!'" +
        emoji_choices.shop_emoji()
    )

    yes_no_response(
        "'So, tell me, are you in need of a wand?' (y/n) \n",
        "'Lovely, let's see what we can find for you!'",
        "'Fine, but you won't get far without one!'",
        "Please enter y or n."
    )


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
        emoji_choices.thinking_emoji() +
        "An animal companion to help you on your quest!" +
        emoji_choices.animal_emoji() +
        "Let's pop into The Magical Menagerie to get one!" +
        emoji_choices.shop_emoji()
    )


def pet_request():
    """
    Asks the player to choose one of four pet types,
    and adds it to the player's inventory
    """
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
        "(a) cat" +
        emoji_choices.cat_emoji() +
        "(b) rat" +
        emoji_choices.rat_emoji() +
        "(c) toad" +
        emoji_choices.toad_emoji() +
        "(d) owl" +
        emoji_choices.owl_emoji()
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
    slowprint(
        "So, now that that's done, let's get to it!" +
        emoji_choices.lightning_emoji() +
        "Grab on to this portkey and let's go to Hogwarts!" +
        emoji_choices.castle_emoji() +
        "Here we are, I hope you're ready!" +
        emoji_choices.luck_emoji() +
        "Let's see now, how do we get inside?" +
        emoji_choices.thinking_emoji()
    )

    door_backstory("first", "the Forbidden Forest")


def first_key_challenge():
    """
    Prompts the player to solve the first key challenge,
    in order to open the first door
    """
    new_line()

    first_key_choices = Abcd(
        "Yes, well done! Your pet will tackle that no problem!",
        "Hmm no, your pet can't do that!"
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

    first_key_input = input("Which option do you pick? \n")

    print("\n")

    if "a" in first_key_input and "{'toad'}" in inventory:
        slowprint(
            first_key_choices.response_correct() +
            emoji_choices.toad_emoji()
        )
        key_main()
    elif "b" in first_key_input and "{'cat'}" in inventory:
        slowprint(
            first_key_choices.response_correct() +
            emoji_choices.cat_emoji()
        )
        key_main()
    elif "c" in first_key_input and "{'rat'}" in inventory:
        slowprint(
            first_key_choices.response_correct() +
            emoji_choices.rat_emoji()
        )
        key_main()
    elif "d" in first_key_input and "{'owl'}" in inventory:
        slowprint(
            first_key_choices.response_correct() +
            emoji_choices.owl_emoji()
        )
        key_main()
    elif "a" in first_key_input and "{'toad'}" not in inventory:
        slowprint(
            first_key_choices.response_incorrect() +
            emoji_choices.animal_emoji()
        )
        exit_game()
    elif "b" in first_key_input and "{'cat'}" not in inventory:
        slowprint(
            first_key_choices.response_incorrect() +
            emoji_choices.animal_emoji()
        )
        exit_game()
    elif "c" in first_key_input and "{'rat'}" not in inventory:
        slowprint(
            first_key_choices.response_incorrect() +
            emoji_choices.animal_emoji()
        )
        exit_game()
    elif "d" in first_key_input and "{'owl'}" not in inventory:
        slowprint(
            first_key_choices.response_incorrect() +
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
        "a pygmy puff",
        "Fred and George Weasley",
        "they",
        "We"
        )

    first_room.room_backstory()


def first_item_question():
    """
    Prompts the player to solve the first room question,
    in order to obtain an item required to open the
    next door
    """
    new_line()

    first_item_choices = Abcd(
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

    first_item_input = input(
        "'Which item is available for sale at Weasleys' Wizard Wheezes?' \n"
        )

    print("\n")

    if "c" in first_item_input:
        slowprint(
            first_item_choices.response_correct() +
            emoji_choices.map_emoji()
        )
        add_to_inventory("Marauder's Map")
    elif "a" in first_item_input:
        slowprint(
            first_item_choices.response_incorrect() +
            emoji_choices.sad_emoji()
        )
        exit_game()
    elif "b" in first_item_input:
        slowprint(
            first_item_choices.response_incorrect() +
            emoji_choices.sad_emoji()
        )
        exit_game()
    elif "d" in first_item_input:
        slowprint(
            first_item_choices.response_incorrect() +
            emoji_choices.sad_emoji()
        )
        exit_game()
    else:
        slowprint(
            abcd_other_responses.other_response() +
            emoji_choices.neutral_emoji()
        )
        first_item_question()

    new_line()

    door_backstory("second", "a secret passage")

    slowprint(
        "Maybe your map could help you here..." +
        emoji_choices.map_emoji()
    )


def second_key_challenge():
    """
    Prompts the player to solve the second key challenge,
    in order to open the second door
    """
    new_line()

    second_key_choices = Abcd(
        "Yes, well done! Now you can get to the secret passage!",
        "Hmm no, that's not the right phrase!"
    )

    slowprint(
        "Out of the following phrases: \n"
        "(a) OK Marauder's Map... "
        "\U0001F4DC \n"
        "(b) I solemnly swear that I am up to no good. "
        "\U0001F607 \n"
        "(c) Show yourself! "
        "\U0001F9D0 \n"
        "(d) Mischief managed. "
        "\U0001F608"
    )

    second_key_input = input(
        "Which one reveals the map? \n"
        )

    print("\n")

    if "b" in second_key_input:
        slowprint(
            second_key_choices.response_correct() +
            emoji_choices.happy_emoji()
        )
        key_main()
    elif "a" in second_key_input:
        slowprint(
            second_key_choices.response_incorrect() +
            emoji_choices.sad_emoji()
        )
        exit_game()
    elif "c" in second_key_input:
        slowprint(
            second_key_choices.response_incorrect() +
            emoji_choices.sad_emoji()
        )
        exit_game()
    elif "d" in second_key_input:
        slowprint(
            second_key_choices.response_incorrect() +
            emoji_choices.sad_emoji()
        )
        exit_game()
    else:
        slowprint(
            abcd_other_responses.other_response() +
            emoji_choices.neutral_emoji()
        )
        second_key_challenge()


def second_room_backstory():
    """
    Runs second room backstory
    """
    new_line()

    second_room = Room(
        "second",
        "Crookshanks",
        "Hermione Granger",
        "she",
        "I"
        )

    second_room.room_backstory()


def second_item_question():
    """
    Prompts the player to solve the second room question,
    in order to obtain an item required to open the
    next door
    """
    new_line()

    second_item_choices = Abcd(
        "'I see you've done your reading! I think you'll like this item...'",
        "'Nope, that represents a different Hogwarts House!'"
    )

    slowprint(
        "Out of the following animals: \n"
        "(a) Eagle. "
        "\U0001F985 \n"
        "(b) Snake. "
        "\U0001F40D \n"
        "(c) Badger. "
        "\U0001F9A1 \n"
        "(d) Lion. "
        "\U0001F981"
    )

    second_item_input = input(
        "'Which one represents Gryffindor?' \n"
        )

    print("\n")

    if "d" in second_item_input:
        slowprint(
            second_item_choices.response_correct() +
            emoji_choices.potion_emoji()
        )
        add_to_inventory("Polyjuice Potion")
    elif "a" in second_item_input:
        slowprint(
            second_item_choices.response_incorrect() +
            emoji_choices.sad_emoji()
        )
        exit_game()
    elif "b" in second_item_input:
        slowprint(
            second_item_choices.response_incorrect() +
            emoji_choices.sad_emoji()
        )
        exit_game()
    elif "c" in second_item_input:
        slowprint(
            second_item_choices.response_incorrect() +
            emoji_choices.sad_emoji()
        )
        exit_game()
    else:
        slowprint(
            abcd_other_responses.other_response() +
            emoji_choices.neutral_emoji()
        )
        second_item_question()

    new_line()

    door_backstory("third", "the staffroom")

    slowprint(
        "Maybe your potion could help you here..." +
        emoji_choices.potion_emoji()
    )


def third_key_challenge():
    """
    Prompts the player to solve the third key challenge,
    in order to open the third door
    """
    new_line()

    third_key_choices = Abcd(
        "Yes, well done! Now you can get into the staffroom as a teacher!",
        "Hmm no, that's from a different potion!"
    )

    slowprint(
        "Out of the following ingredients: \n"
        "(a) DNA of the person you want to become. "
        "\U0001F487 \n"
        "(b) Asian dragon hair. "
        "\U0001F432 \n"
        "(c) Eyeball. "
        "\U0001F440 \n"
        "(d) Peacock feather. "
        "\U0001F99A"
    )

    third_key_input = input(
        "Which one is needed to complete the Polyjuice Potion? \n"
        )

    print("\n")

    if "a" in third_key_input:
        slowprint(
            third_key_choices.response_correct() +
            emoji_choices.happy_emoji()
        )
        key_main()
    elif "b" in third_key_input:
        slowprint(
            third_key_choices.response_incorrect() +
            emoji_choices.sad_emoji()
        )
        exit_game()
    elif "c" in third_key_input:
        slowprint(
            third_key_choices.response_incorrect() +
            emoji_choices.sad_emoji()
        )
        exit_game()
    elif "d" in third_key_input:
        slowprint(
            third_key_choices.response_incorrect() +
            emoji_choices.sad_emoji()
        )
        exit_game()
    else:
        slowprint(
            abcd_other_responses.other_response() +
            emoji_choices.neutral_emoji()
        )
        third_key_challenge()


def third_room_backstory():
    """
    Runs third room backstory
    """
    new_line()

    third_room = Room(
        "third",
        "Fawkes",
        "Albus Dumbledore",
        "he",
        "I"
        )

    third_room.room_backstory()


def third_item_question():
    """
    Prompts the player to solve the third room question,
    in order to obtain an item required to open the
    next door
    """
    new_line()

    third_item_choices = Abcd(
        "'I see you know me well! I think you'll like this item...'",
        "'No, I really don't care for those!'"
    )

    slowprint(
        "Out of the following sweets: \n"
        "(a) Blood-Flavoured Lollipops. "
        "\U0001F36D \n"
        "(b) Chocolate Frogs. "
        "\U0001F36B \n"
        "(c) Bertie Bott's Every-Flavour Beans. "
        "\U0001F36C \n"
        "(d) Sherbet Lemons. "
        "\U0001F34B"
    )

    third_item_input = input(
        "'Which one is my favourite?' \n"
        )

    print("\n")

    if "d" in third_item_input:
        slowprint(
            third_item_choices.response_correct() +
            emoji_choices.cloak_emoji()
        )
        add_to_inventory("Cloak of Invisibility")
    elif "a" in third_item_input:
        slowprint(
            third_item_choices.response_incorrect() +
            emoji_choices.sad_emoji()
        )
        exit_game()
    elif "b" in third_item_input:
        slowprint(
            third_item_choices.response_incorrect() +
            emoji_choices.sad_emoji()
        )
        exit_game()
    elif "c" in third_item_input:
        slowprint(
            third_item_choices.response_incorrect() +
            emoji_choices.sad_emoji()
        )
        exit_game()
    else:
        slowprint(
            abcd_other_responses.other_response() +
            emoji_choices.neutral_emoji()
        )
        third_item_question()

    new_line()

    door_backstory("fourth", "the dungeon with the troll")

    slowprint(
        "Maybe your cloak could help you here..." +
        emoji_choices.cloak_emoji()
    )


def fourth_key_challenge():
    """
    Prompts the player to solve the fourth key challenge,
    in order to open the fourth door
    """
    new_line()

    fourth_key_choices = Abcd(
        "Yes, well done! Now you can sneak past the troll in the dungeon!",
        "Hmm no, this one can reveal the cloak wearer!"
    )

    slowprint(
        "Out of the following: \n"
        "(a) Marauder's Map. "
        "\U0001F4DC \n"
        "(b) Death. "
        "\U0001F480 \n"
        "(c) Magical Eyes. "
        "\U0001F440 \n"
        "(d) Dementors. "
        "\U0001F311"
    )

    fourth_key_input = input(
        "Which one can not see past the Cloak of Invisibility? \n"
        )

    print("\n")

    if "b" in fourth_key_input:
        slowprint(
            fourth_key_choices.response_correct() +
            emoji_choices.happy_emoji()
        )
        key_main()
    elif "a" in fourth_key_input:
        slowprint(
            fourth_key_choices.response_incorrect() +
            emoji_choices.sad_emoji()
        )
        exit_game()
    elif "c" in fourth_key_input:
        slowprint(
            fourth_key_choices.response_incorrect() +
            emoji_choices.sad_emoji()
        )
        exit_game()
    elif "d" in fourth_key_input:
        slowprint(
            fourth_key_choices.response_incorrect() +
            emoji_choices.sad_emoji()
        )
        exit_game()
    else:
        slowprint(
            abcd_other_responses.other_response() +
            emoji_choices.neutral_emoji()
        )
        fourth_key_challenge()


def fourth_room_backstory():
    """
    Runs fourth room backstory
    """
    slowprint(
        "You enter the fourth room and look around..." +
        emoji_choices.door_emoji() +
        "Hang on, is that Nagini?! " +
        emoji_choices.snake_emoji() +
        "That can only mean one thing..." +
        emoji_choices.darkmoon_emoji() +
        "It's Lord Voldemort!" +
        emoji_choices.evil_emoji() +
        "'Who dares challenge me?!'" +
        emoji_choices.wizard_emoji() +
        "'Show me what you've got, I dare you...'" +
        emoji_choices.lightning_emoji() +
        "You'll need to choose the correct spells in order to beat him!" +
        emoji_choices.spell_emoji()
    )


def first_spell_challenge():
    """
    Prompts the player to choose the correct first spell
    in order to beat Voldemort
    """
    new_line()

    first_spell_choices = Abcd(
        "Yes, well done! That will remove his wand!",
        "Bad luck, that spell won't harm him!"
    )

    slowprint(
        "Out of the following spells: \n"
        "(a) Alohomora! "
        "\U0001F511 \n"
        "(b) Lumos! "
        "\U0001F4A1 \n"
        "(c) Expelliarmus! "
        "\U0001F320 \n"
        "(d) Expecto Patronum! "
        "\U0001F43E"
    )

    first_spell_input = input(
        "Which do you cast first? \n"
        )

    print("\n")

    if "c" in first_spell_input:
        slowprint(
            first_spell_choices.response_correct() +
            emoji_choices.happy_emoji()
        )
    elif "a" in first_spell_input:
        slowprint(
            first_spell_choices.response_incorrect() +
            emoji_choices.sad_emoji()
        )
        exit_game()
    elif "b" in first_spell_input:
        slowprint(
            first_spell_choices.response_incorrect() +
            emoji_choices.sad_emoji()
        )
        exit_game()
    elif "d" in first_spell_input:
        slowprint(
            first_spell_choices.response_incorrect() +
            emoji_choices.sad_emoji()
        )
        exit_game()
    else:
        slowprint(
            abcd_other_responses.other_response() +
            emoji_choices.neutral_emoji()
        )
        first_spell_challenge()


def second_spell_challenge():
    """
    Prompts the player to choose the correct second spell
    in order to beat Voldemort
    """
    new_line()

    second_spell_choices = Abcd(
        "Yes, well done! That will defeat him!",
        "Bad luck, that spell won't harm him!"
    )

    slowprint(
        "Out of the following spells: \n"
        "(a) Avada Kedavra! "
        "\U0001F480 \n"
        "(b) Wingardium Leviosa! "
        "\U0001F9F9 \n"
        "(c) Reparo! "
        "\U0001FA79 \n"
        "(d) Riddikulus! "
        "\U0001F921"
    )

    second_spell_input = input(
        "Which do you cast second? \n"
        )

    print("\n")

    if "a" in second_spell_input:
        slowprint(
            second_spell_choices.response_correct() +
            emoji_choices.happy_emoji()
        )
        win_game()
    elif "b" in second_spell_input:
        slowprint(
            second_spell_choices.response_incorrect() +
            emoji_choices.sad_emoji()
        )
        exit_game()
    elif "c" in second_spell_input:
        slowprint(
            second_spell_choices.response_incorrect() +
            emoji_choices.sad_emoji()
        )
        exit_game()
    elif "d" in second_spell_input:
        slowprint(
            second_spell_choices.response_incorrect() +
            emoji_choices.sad_emoji()
        )
        exit_game()
    else:
        slowprint(
            abcd_other_responses.other_response() +
            emoji_choices.neutral_emoji()
        )
        second_spell_challenge()


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
    second_key_challenge()
    second_room_backstory()
    second_item_question()
    third_key_challenge()
    third_room_backstory()
    third_item_question()
    fourth_key_challenge()
    fourth_room_backstory()
    first_spell_challenge()
    second_spell_challenge()


# Calls main game functions
main_one()
