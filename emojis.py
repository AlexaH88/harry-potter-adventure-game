"""
Contains a class for all the emojis in the game
"""


class Emoji:
    """
    Emoji class
    """
    def __init__(self):
        """
        Creates an instance of Emoji
        """
        self.lightning = " \u26A1 \n"
        self.castle = " \U0001F3F0 \n"
        self.surprised = " \U0001F632 \n"
        self.wizard = " \U0001F9D9 \n"
        self.world = " \U0001F30D \n"

    def lightning_emoji(self):
        """
        Runs lightning emoji
        """
        return f"{self.lightning}"

    def castle_emoji(self):
        """
        Runs castle emoji
        """
        return f"{self.castle}"

    def surprised_emoji(self):
        """
        Runs surprised emoji
        """
        return f"{self.surprised}"

    def wizard_emoji(self):
        """
        Runs wizard emoji
        """
        return f"{self.wizard}"

    def world_emoji(self):
        """
        Runs world emoji
        """
        return f"{self.world}"
