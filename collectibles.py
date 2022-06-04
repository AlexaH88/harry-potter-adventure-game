# Contains classes for all the collectibles in the game

inventory = []


class Pet:
    """
    Pet class
    """
    def __init__(self, kind, skill):
        self.kind = kind
        self.skill = skill

    def choice_confirmation(self):
        """
        Confirms pet choice
        """
        return f"Great choice! You'll love your {self.kind}!"

    def description(self):
        """
        Describes the pet
        """
        return f"{self.kind}s are known for their impressive \
        {self.skill} skills. Use this wisely!"
    
    def add_pet_to_inventory(self):
        """
        Adds pet to the player's inventory
        """
        inventory.append({self.kind})
        return f"Your {self.kind} was added to your inventory."
