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


class AbcdChallenge:
    """
    AbcdChallenge questions class
    """
    def __init__(
        self,
        answer_a_correct,
        answer_b_correct,
        answer_c_correct,
        answer_d_correct,
        answer_incorrect,
    ):
        """
        Creates an instance of AbcdChallenge
        """
        self.answer_a_correct = answer_a_correct
        self.answer_b_correct = answer_b_correct
        self.answer_c_correct = answer_c_correct
        self.answer_d_correct = answer_d_correct
        self.answer_incorrect = answer_incorrect

    def a_response_correct(self):
        """
        Runs response to player answering (a) correctly
        """
        return f"{self.answer_a_correct}"

    def b_response_correct(self):
        """
        Runs response to player answering (b) correctly
        """
        return f"{self.answer_b_correct}"

    def c_response_correct(self):
        """
        Runs response to player answering (c) correctly
        """
        return f"{self.answer_c_correct}"

    def d_response_correct(self):
        """
        Runs response to player answering (d) correctly
        """
        return f"{self.answer_d_correct}"

    def response_incorrect(self):
        """
        Runs response to player answering incorrectly
        """
        return f"{self.answer_incorrect}"


class AbcdQuestion:
    """
    AbcdQuestion questions class
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
