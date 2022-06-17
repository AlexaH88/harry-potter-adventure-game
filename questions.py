"""
Contains functions and classes for the questions in the game
"""


from emojis import Emoji
from gameplay import slowprint, exit_game


emoji_choices = Emoji()


class YesNoResponse:
    """
    YesNoResponse class
    """
    def __init__(self, answer_yes, answer_no):
        """
        Creates an instance of YesNoResponse
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


class AbcdResponse:
    """
    AbcdResponse class
    """
    def __init__(
        self,
        answer_correct,
        answer_incorrect,
    ):
        """
        Creates an instance of AbcdResponse
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


class AbcdOtherResponse:
    """
    AbcdOtherResponse class
    """
    def __init__(self):
        """
        Creates an instance of AbcdOtherResponse
        """
        self.answer_other = "Please enter a, b, c, or d."

    def other_response(self):
        """
        Runs response to player answering with any other key
        """
        return f"{self.answer_other}"


def yes_no_response(
    input_question,
    answer_yes,
    answer_no,
    answer_other
):
    """
    Runs if statement on yes no responses
    """
    user_input = input(input_question)

    if user_input == "y":
        slowprint(
            answer_yes +
            emoji_choices.happy_emoji()
        )
    elif user_input == "n":
        slowprint(
            answer_no +
            emoji_choices.sad_emoji()
        )
        exit_game()
    else:
        slowprint(
            answer_other +
            emoji_choices.neutral_emoji()
        )
        yes_no_response(input_question, answer_yes, answer_no, answer_other)


def abcd_response(
    correct,
    input_question,
    answer_correct,
    answer_incorrect,
    answer_other
):
    """
    Runs if statement on abcd responses
    """
    user_input = input(input_question)

    if "a" in user_input and "a" in correct:
        slowprint(
            answer_correct +
            emoji_choices.happy_emoji()
        )
    elif "b" in user_input and "b" in correct:
        slowprint(
            answer_correct +
            emoji_choices.happy_emoji()
        )
    elif "c" in user_input and "c" in correct:
        slowprint(
            answer_correct +
            emoji_choices.happy_emoji()
        )
    elif "d" in user_input and "d" in correct:
        slowprint(
            answer_correct +
            emoji_choices.happy_emoji()
        )
    elif "a" in user_input and "a" not in correct:
        slowprint(
            answer_incorrect +
            emoji_choices.sad_emoji()
        )
        exit_game()
    elif "b" in user_input and "b" not in correct:
        slowprint(
            answer_incorrect +
            emoji_choices.sad_emoji()
        )
        exit_game()
    elif "c" in user_input and "c" not in correct:
        slowprint(
            answer_incorrect +
            emoji_choices.sad_emoji()
        )
        exit_game()
    elif "d" in user_input and "d" not in correct:
        slowprint(
            answer_incorrect +
            emoji_choices.sad_emoji()
        )
        exit_game()
    else:
        slowprint(
            answer_other +
            emoji_choices.neutral_emoji()
        )
        abcd_response(
            correct,
            input_question,
            answer_correct,
            answer_incorrect,
            answer_other
        )
