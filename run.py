"""
Runs the game
"""


# Imports modules
import random
from collectibles import (
                        inventory,
                        Wand,
                        Pet,
                        key_main,
                        add_to_inventory
)
from questions import (
                    YesNoResponse,
                    AbcdResponse,
                    AbcdOtherResponse,
                    yes_no_response,
                    abcd_response,
)
from gameplay import (
                    slowprint,
                    exit_game,
                    win_game,
                    room_backstory,
                    door_backstory
)
from emojis import Emoji


# Declares variables
emoji_choices = Emoji()
abcd_other_responses = AbcdOtherResponse()


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
    yes_no_response(
        "Ready to face up to the challenge? (y/n) \n",
        "Great choice, let the adventure begin!",
        "That's a shame, maybe next time!",
        "Please enter y or n."
    )


def choose_game_instructions():
    """
    Asks the player if they want to read the game instructions or not
    """
    game_instructions_responses = YesNoResponse(
        "Right, let me explain the game to you!",
        "Ok, let's carry on with the quest!"
        )

    game_instructions_input = input(
        "Would you like to read the game instructions first? (y/n) \n"
        )

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
    player_name_input = input("Choose your witch or wizard name: \n")

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
        emoji_choices.oldman_emoji() +
        "'Welcome to my shop, you've come to the right place!'" +
        emoji_choices.shop_emoji()
    )


def wand_request():
    """
    Asks the player to request a wand
    """
    yes_no_response(
        "'So, tell me, are you in need of a wand?' (y/n) \n",
        "'Lovely, let's see what we can find for you!'",
        "'Fine, but you won't get far without one!'",
        "Please enter y or n."
    )

    slowprint(
        "Ollivander looks you up and down, studying you carefully..." +
        emoji_choices.monocle_emoji()
    )


def assign_wand():
    """
    Randomly assigns the player one of three wand options,
    and adds it to the player's inventory
    """
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
        "a Phoenix feather",
        "nice and supple")

    albus = Wand(
        "Albus Dumbledore's wand",
        "15 inches",
        "elder",
        "a Thestral tail hair",
        "the most powerful wand ever to exist")

    rubeus = Wand(
        "Rubeus Hagrid's wand",
        "16 inches",
        "oak",
        "an unknown",
        "rather bendy")

    if "Harry Potter's wand" in random_wand_options:
        slowprint(
            harry.description() +
            emoji_choices.harrywand_emoji() +
            harry.add_wand_to_inventory() +
            emoji_choices.backpack_emoji()
        )
    elif "Albus Dumbledore's wand" in random_wand_options:
        slowprint(
            albus.description() +
            emoji_choices.albuswand_emoji() +
            albus.add_wand_to_inventory() +
            emoji_choices.backpack_emoji()
        )
    elif "Rubeus Hagrid's wand" in random_wand_options:
        slowprint(
            rubeus.description() +
            emoji_choices.rubeuswand_emoji() +
            rubeus.add_wand_to_inventory() +
            emoji_choices.backpack_emoji()
        )


def pet_backstory():
    """
    Runs backstory on The Magical Menagerie and player pet selection
    """
    slowprint(
        "Right, what's next?" +
        emoji_choices.thinking_emoji() +
        "An animal companion to help you on your quest!" +
        emoji_choices.animal_emoji() +
        "Let's pop into The Magical Menagerie to get one!" +
        emoji_choices.shop_emoji() +
        "'Welcome to my shop, let me show you what lovely pets we've got!'" +
        emoji_choices.oldlady_emoji()
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

    if "a" in ask_for_pet:
        slowprint(
            cat.choice_confirmation() +
            emoji_choices.cat_emoji() +
            cat.description() +
            emoji_choices.animal_emoji() +
            cat.add_pet_to_inventory() +
            emoji_choices.backpack_emoji()
        )
    elif "b" in ask_for_pet:
        slowprint(
            rat.choice_confirmation() +
            emoji_choices.rat_emoji() +
            rat.description() +
            emoji_choices.animal_emoji() +
            rat.add_pet_to_inventory() +
            emoji_choices.backpack_emoji()
        )
    elif "c" in ask_for_pet:
        slowprint(
            toad.choice_confirmation() +
            emoji_choices.toad_emoji() +
            toad.description() +
            emoji_choices.animal_emoji() +
            toad.add_pet_to_inventory() +
            emoji_choices.backpack_emoji()
        )
    elif "d" in ask_for_pet:
        slowprint(
            owl.choice_confirmation() +
            emoji_choices.owl_emoji() +
            owl.description() +
            emoji_choices.animal_emoji() +
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
    first_key_choices = AbcdResponse(
        "Yes, well done! Your pet will tackle that no problem!",
        "Hmm no, your pet can't do that!"
    )

    slowprint(
        "But there are several obstacles in the way: \n"
        "(a) A pond, perfect for swimming across..." +
        emoji_choices.pond_emoji() +
        "(b) A big tree, perfect for climbing up..." +
        emoji_choices.tree_emoji() +
        "(c) An ivy plant, perfect for chewing through..." +
        emoji_choices.ivy_emoji() +
        "(d) A small mountain, perfect for flying over..." +
        emoji_choices.mountain_emoji()
    )

    slowprint(
        "Maybe your pet could help you here..." +
        emoji_choices.animal_emoji()
        )

    first_key_input = input("Which option do you pick? \n")

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
    room_backstory(
        "first",
        "a pygmy puff",
        "Fred and George Weasley",
        "they",
        "We"
    )


def first_item_question():
    """
    Prompts the player to solve the first room question,
    in order to obtain an item required to open the
    next door
    """
    first_item_choices = AbcdResponse(
        "'I see you're a fan! I think you'll like this item...'",
        "'Nope, that's from a different shop in Diagon Alley!'"
    )

    slowprint(
        "Out of the following items: \n"
        "(a) The Monster Book of Monsters." +
        emoji_choices.book_emoji() +
        "(b) Dungbombs." +
        emoji_choices.bomb_emoji() +
        "(c) Extendable Ears." +
        emoji_choices.ear_emoji() +
        "(d) Butterbeer." +
        emoji_choices.beer_emoji()
    )

    first_item_input = input(
        "'Which item is available for sale at Weasleys' Wizard Wheezes?' \n"
        )

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
    second_key_choices = AbcdResponse(
        "Yes, well done! Now you can get to the secret passage!",
        "Hmm no, that's not the right phrase!"
    )
    slowprint(
        "Out of the following phrases: \n"
        "(a) OK Marauder's Map..." +
        emoji_choices.map_emoji() +
        "(b) I solemnly swear that I am up to no good." +
        emoji_choices.angel_emoji() +
        "(c) Show yourself!" +
        emoji_choices.monocle_emoji() +
        "(d) Mischief managed." +
        emoji_choices.evil_emoji()
    )
    second_key_input = input(
        "Which one reveals the map? \n"
        )
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
    room_backstory(
        "second",
        "Crookshanks",
        "Hermione Granger",
        "she",
        "I"
    )


def second_item_question():
    """
    Prompts the player to solve the second room question,
    in order to obtain an item required to open the
    next door
    """
    second_item_choices = AbcdResponse(
        "'I see you've done your reading! I think you'll like this item...'",
        "'Nope, that represents a different Hogwarts House!'"
    )

    slowprint(
        "Out of the following animals: \n"
        "(a) Eagle." +
        emoji_choices.eagle_emoji() +
        "(b) Snake." +
        emoji_choices.snake_emoji() +
        "(c) Badger." +
        emoji_choices.badger_emoji() +
        "(d) Lion." +
        emoji_choices.lion_emoji()
    )

    second_item_input = input(
        "'Which one represents Gryffindor?' \n"
        )

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
    third_key_choices = AbcdResponse(
        "Yes, well done! Now you can get into the staffroom as a teacher!",
        "Hmm no, that's from a different potion!"
    )

    slowprint(
        "Out of the following ingredients: \n"
        "(a) DNA of the person you want to become." +
        emoji_choices.hair_emoji() +
        "(b) Asian dragon hair." +
        emoji_choices.dragon_emoji() +
        "(c) Eyeball." +
        emoji_choices.eye_emoji() +
        "(d) Peacock feather." +
        emoji_choices.peacock_emoji()
    )

    third_key_input = input(
        "Which one is needed to complete the Polyjuice Potion? \n"
        )

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
    room_backstory(
        "third",
        "Fawkes",
        "Albus Dumbledore",
        "he",
        "I"
    )


def third_item_question():
    """
    Prompts the player to solve the third room question,
    in order to obtain an item required to open the
    next door
    """
    third_item_choices = AbcdResponse(
        "'I see you know me well! I think you'll like this item...'",
        "'No, I really don't care for those!'"
    )

    slowprint(
        "Out of the following sweets: \n"
        "(a) Blood-Flavoured Lollipops." +
        emoji_choices.lollipop_emoji() +
        "(b) Chocolate Frogs." +
        emoji_choices.chocolate_emoji() +
        "(c) Bertie Bott's Every-Flavour Beans." +
        emoji_choices.sweetie_emoji() +
        "(d) Sherbet Lemons." +
        emoji_choices.lemon_emoji()
    )

    third_item_input = input(
        "'Which one is my favourite?' \n"
        )

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
    fourth_key_choices = AbcdResponse(
        "Yes, well done! Now you can sneak past the troll in the dungeon!",
        "Hmm no, this one can reveal the cloak wearer!"
    )

    slowprint(
        "Out of the following: \n"
        "(a) Marauder's Map." +
        emoji_choices.map_emoji() +
        "(b) Death." +
        emoji_choices.skull_emoji() +
        "(c) Magical Eyes." +
        emoji_choices.eye_emoji() +
        "(d) Dementors." +
        emoji_choices.darkmoon_emoji()
    )

    fourth_key_input = input(
        "Which one can not see past the Cloak of Invisibility? \n"
        )

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
    slowprint(
        "Out of the following spells: \n"
        "(a) Alohomora!" +
        emoji_choices.key_emoji() +
        "(b) Lumos!" +
        emoji_choices.lightbulb_emoji() +
        "(c) Expelliarmus!" +
        emoji_choices.spell_emoji() +
        "(d) Expecto Patronum!" +
        emoji_choices.animal_emoji()
    )

    abcd_response(
        "c",
        "Which do you cast first? \n",
        "Yes, well done! That will remove his wand!",
        "Bad luck, that spell won't harm him!",
        "Please enter a, b, c, or d."
    )


def second_spell_challenge():
    """
    Prompts the player to choose the correct second spell
    in order to beat Voldemort
    """
    second_spell_choices = AbcdResponse(
        "Yes, well done! That will defeat him!",
        "Bad luck, that spell won't harm him!"
    )

    slowprint(
        "Out of the following spells: \n"
        "(a) Avada Kedavra!" +
        emoji_choices.skull_emoji() +
        "(b) Wingardium Leviosa!" +
        emoji_choices.broom_emoji() +
        "(c) Reparo!" +
        emoji_choices.plaster_emoji() +
        "(d) Riddikulus!" +
        emoji_choices.clown_emoji()
    )

    second_spell_input = input(
        "Which do you cast second? \n"
        )

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
