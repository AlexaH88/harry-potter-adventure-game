"""
Contains classes for the questions in the game
"""


class YesNo:
    """
    YesNo questions class
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


class Abcd:
    """
    Abcd questions class
    """
    def __init__(self, answer_a, answer_b, answer_c, answer_d):
        """
        Creates an instance of Abcd
        """
        self.answer_a = answer_a
        self.answer_b = answer_b
        self.answer_c = answer_c
        self.answer_d = answer_d

    def a_response(self):
        """
        Runs response to player answering (a)
        """
        return f"{self.answer_a}"

    def b_response(self):
        """
        Runs response to player answering (b)
        """
        return f"{self.answer_b}"

    def c_response(self):
        """
        Runs response to player answering (c)
        """
        return f"{self.answer_c}"

    def d_response(self):
        """
        Runs response to player answering (d)
        """
        return f"{self.answer_d}"


class AbcdOther:
    """
    AbcdOther questions class
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
