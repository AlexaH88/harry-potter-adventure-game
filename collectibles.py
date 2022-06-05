"""
Contains classes for all the collectibles in the game
"""


inventory = []


class Wand:
    """
    Wand class
    """
    def __init__(self, owner, length, wood, core, characteristic, emoji):
        """
        Creates an instance of Wand
        """
        self.owner = owner
        self.length = length
        self.wood = wood
        self.core = core
        self.characteristic = characteristic
        self.emoji = emoji

    def description(self):
        """
        Describes the wand
        """
        return (
            f"'This wand is {self.length} long, "
            f"is made with {self.wood} wood, "
            f"has a(n) {self.core} core, "
            f"and is {self.characteristic}!' "
            f"{self.emoji} \n"
        )

    def add_wand_to_inventory(self):
        """
        Adds wand to the player's inventory
        """
        inventory.append({self.owner})
        return (
            f"{self.owner} was added to your inventory. "
            "\U0001F392 \n"
        )


class Pet:
    """
    Pet class
    """
    def __init__(self, kind, skill, emoji):
        """
        Creates an instance of Pet
        """
        self.kind = kind
        self.skill = skill
        self.emoji = emoji

    def choice_confirmation(self):
        """
        Confirms pet choice
        """
        return f"\n'Great choice! You'll love your {self.kind}!' {self.emoji} "

    def description(self):
        """
        Describes the pet
        """
        return (
            f"'{self.kind.capitalize()}s are known for their impressive "
            f"{self.skill} skills. Use this wisely!' \n"
        )

    def add_pet_to_inventory(self):
        """
        Adds pet to the player's inventory
        """
        inventory.append(str({self.kind}))
        return f"Your {self.kind} was added to your inventory. \U0001F392 \n"
