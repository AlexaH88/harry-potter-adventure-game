# Contains classes for all the collectibles in the game

import random


inventory = []


class Wand:
    """
    Wand class
    """
    def __init__(self, owner, length, wood, core, flexibility):
        """
        Creates an instance of Wand
        """
        self.owner = owner
        self.length = length
        self.wood = wood
        self.core = core
        self.flexibility = flexibility

    def random_selection(self):
        """
        Randomly assigns the player one of three wand options
        """
        return random.choice({self.owner}) + "'will suit you nicely!'"

    def description(self):
        """
        Describes the wand
        """
        return f'"This wand is {self.length} long, \
            is made with {self.wood} wood, \
                has a {self.core} core, \
                    and is {self.flexibility}."'

    def add_wand_to_inventory(self):
        """
        Adds wand to the player's inventory
        """
        inventory.append({self.owner})
        return f"{self.owner} was added to your inventory."


class Pet:
    """
    Pet class
    """
    def __init__(self, kind, skill):
        """
        Creates an instance of Pet
        """
        self.kind = kind
        self.skill = skill

    def choice_confirmation(self):
        """
        Confirms pet choice
        """
        return f"'Great choice! You'll love your {self.kind}!'"

    def description(self):
        """
        Describes the pet
        """
        return f"'{self.kind}s are known for their impressive \
        {self.skill} skills. Use this wisely!'"

    def add_pet_to_inventory(self):
        """
        Adds pet to the player's inventory
        """
        inventory.append({self.kind})
        return f"Your {self.kind} was added to your inventory."
