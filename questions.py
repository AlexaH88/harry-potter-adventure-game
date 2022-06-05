"""
Contains classes for all the questions in the game
"""


class YesNo:
    """
    Yes No questions class
    """
    def __init__(self, answer_yes, answer_no, answer_other):
        """
        Creates an instance of Yes No questions
        """
        self.answer_yes = answer_yes
        self.answer_no = answer_no
        self.answer_other = answer_other

    def yes_response(self):
        """
        Runs response to player answering yes (y)
        """
        return (
            f"\n {self.answer_yes} \U0001F642 \n"
        )

    def no_response(self):
        """
        Runs response to player answering no (n)
        """
        return (
            f"\n {self.answer_no} \U0001F641 \n"
        )

    def other_response(self):
        """
        Runs response to player answering eith any other key
        """
        return (
            f"\n {self.answer_other} \U0001F610 \n"
        )
