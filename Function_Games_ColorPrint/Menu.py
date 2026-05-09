"""Prints a colored banner menu using ANSI escape sequences via colorama."""
import colorama


def banner_text(text: str = " ", screen_width: int = 80) -> None:
    """
    Prints user text, plus desired banner

    :param text: This function prompts the user for input to determine both a banner
    and text to put inside of the banner. If the string input is too long
    an error will appear to notify the user it will not fit. To add border,
    just input `*` , and a top or bottom border should appear.
    :param screen_width: Screen width is set to a default of 80, or width - 4
    for actual text (includes ** on both sides)
    :raises ValueError: If the string input is too long to fit
    """
    if len(text) > screen_width - 4:
        raise ValueError("String {0} is larger than specified width {1}"
                         .format(text, screen_width))

    if text == "*":
        color_print(("*" * screen_width), CYAN)
    else:
        output_string = "**{0}**".format(text.center(screen_width - 4))
        color_print(output_string, YELLOW)


def color_print(text: str, *effects: str) -> None:
    """
    Print `text` using the ANSI sequences to change color, etc

    :param text: The text to print
    :param effects: The effect we want. One of the
        constants defined at the start of this module
    """
    effect_string = "".join(effects)
    output_string = "{0}{1}{2}".format(effect_string, text, RESET)
    print(output_string)


BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'

BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'

banner_text("*")
banner_text("Choose a game to play")
banner_text("1. Hangman")
banner_text("2. Fizz Buzz")
banner_text("3. Guessing Game")
banner_text("*")
