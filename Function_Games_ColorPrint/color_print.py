"""Demonstrates ANSI color and effect sequences using colorama for cross-platform support."""
import colorama

BLACK = '[30m'
RED = '[31m'
GREEN = '[32m'
YELLOW = '[33m'
BLUE = '[34m'
MAGENTA = '[35m'
CYAN = '[36m'
WHITE = '[37m'
RESET = '[0m'

BOLD = '[1m'
UNDERLINE = '[4m'
REVERSE = '[7m'


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


colorama.init()
color_print("Hello, Red in bold", RED, BOLD)
print("This should be in the default terminal color")
color_print("Hello, Blue reversed", BLUE, REVERSE)
color_print("Hello, Blue reversed and underlined", BLUE, REVERSE, UNDERLINE)
color_print("Hello, Blue", BLUE)
color_print("Hello, Yellow bold", YELLOW, BOLD)
color_print("Hello, Bold", BOLD)
color_print("Hello, Underline", UNDERLINE)
color_print("Hello, Reverse", REVERSE)
color_print("Hello, Black", BLACK)
colorama.deinit()
print(CYAN, "cyan")
