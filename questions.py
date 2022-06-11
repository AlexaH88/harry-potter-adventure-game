"""
Contains classes for the questions in the game
"""


# code related to all yes no answers in the game
class YesNo:
    """
    YesNo class
    """
    def __init__(self, answer_yes, answer_no):
        """
        Creates an instance of YesNo
        """
        self.answer_yes = answer_yes
        self.answer_no = answer_no
        self.answer_other = "Please enter y or n."

    def yes_response(self):
        """
        Runs response to player answering yes (y)
        """
        return f"{self.answer_yes}"

    def no_response(self):
        """
        Runs response to player answering no (n)
        """
        return f"{self.answer_no}"

    def other_response(self):
        """
        Runs response to player answering with any other key
        """
        return f"{self.answer_other}"


# code related to all abcd answers in the game
class Abcd:
    """
    Abcd class
    """
    def __init__(
        self,
        answer_correct,
        answer_incorrect,
    ):
        """
        Creates an instance of AbcdQuestion
        """
        self.answer_correct = answer_correct
        self.answer_incorrect = answer_incorrect

    def response_correct(self):
        """
        Runs response to player answering correctly
        """
        return f"{self.answer_correct}"

    def response_incorrect(self):
        """
        Runs response to player answering incorrectly
        """
        return f"{self.answer_incorrect}"


class AbcdOther:
    """
    AbcdOther class
    """
    def __init__(self):
        """
        Creates an instance of AbcdOther
        """
        self.answer_other = "Please enter a, b, c, or d."

    def other_response(self):
        """
        Runs response to player answering with any other key
        """
        return f"{self.answer_other}"
