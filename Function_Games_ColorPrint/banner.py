"""Prints centered banner text with `**` borders at a configurable screen width."""


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
        print("*" * screen_width)
    else:
        output_string = "**{0}**".format(text.center(screen_width - 4))
        print(output_string)


banner_text("*")
banner_text("Apples")
banner_text("This is a longer sentence")
banner_text("This should all be centered in the text")
banner_text()
banner_text("A space is placed above")
banner_text(screen_width=30)            # Defining a specific keyword argument
banner_text("apples")
banner_text("*")
