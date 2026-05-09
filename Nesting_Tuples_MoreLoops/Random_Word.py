"""Pick a random word of 5–8 letters from predefined word lists, then join its characters."""
import random

FIVE_LETTERS = (
    "adult", "apple", "beach", "board", "brain", "chest", "death",
    "earth", "fight", "heart", "group", "hotel", "issue", "novel", "range",
)
SIX_LETTERS = (
    "branch", "career", "casual", "coffee", "damage", "dealer", "editor",
    "effect", "ground", "guilty", "latter", "leader", "market", "person", "reward",
)
SEVEN_LETTERS = (
    "airline", "western", "village", "warrant", "traffic",
    "trouble", "thought", "surface", "supreme", "request",
    "raining", "reality", "profile", "passing", "monitor",
)
EIGHT_LETTERS = (
    "abstract", "activity", "advanced", "colorful", "compound",
    "conflict", "consumer", "disaster", "disposal", "engineer",
    "everyone", "firewall", "hardware", "inmate", "majority",
)

while True:
    number = random.randint(5, 8)

    separator = ""
    word = [" "] * number

    if number == 5:
        word = random.choice(FIVE_LETTERS)
    elif number == 6:
        word = random.choice(SIX_LETTERS)
    elif number == 7:
        word = random.choice(SEVEN_LETTERS)
    elif number == 8:
        word = random.choice(EIGHT_LETTERS)

    word = separator.join(word)

    break

