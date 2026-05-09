"""Hangman game using ANSI colour codes: pick a random word and give the player 6 letter guesses."""


def hangman_game():
    import random
    import colorama

    reset = '\u001b[0m'
    reverse = '\u001b[7m'
    bold = '\u001b[1m'
    yellow = '\u001b[33m'
    cyan = '\u001b[36m'
    red = '\u001b[31m'

    def color_print(text: str, *effects: str) -> None:
        """Print text with one or more ANSI escape sequences applied."""
        effect_string = "".join(effects)
        output_string = "{0}{1}{2}".format(effect_string, text, reset)
        print(output_string)


    while True:
        five_letters = (
            "adult", "apple", "beach", "board", "brain", "chest", "death",
            "earth", "fight", "heart", "group", "hotel", "issue", "novel", "range",
        )
        six_letters = (
            "branch", "career", "casual", "coffee", "damage", "dealer", "editor",
            "effect", "ground", "guilty", "latter", "leader", "market", "person", "reward",
        )
        seven_letters = (
            "airline", "western", "village", "warrant", "traffic",
            "trouble", "thought", "surface", "supreme", "request",
            "raining", "reality", "profile", "passing", "monitor",
        )
        eight_letters = (
            "abstract", "activity", "advanced", "colorful", "compound",
            "conflict", "consumer", "disaster", "disposal", "engineer",
            "everyone", "firewall", "hardware", "quizzing", "majority",
        )

        number = random.randint(5, 8)

        separator = ""
        word = [" "] * number

        if number == 5:
            word = random.choice(five_letters)
        elif number == 6:
            word = random.choice(six_letters)
        elif number == 7:
            word = random.choice(seven_letters)
        elif number == 8:
            word = random.choice(eight_letters)

        word = separator.join(word)

        hangman = word
        answer = ["_"] * (len(hangman))
        separator = ""
        answer_output = None
        again = None
        control = 1
        guesses = 6

        print(yellow)
        print("Ready to play hangman?")
        print("Press Enter to Begin")
        input()
        print("-" * 80)
        print("There are ", number, " letters in this word")
        print("You have 6 guesses"
              "\nBest of luck!")
        print("_" * 80)
        print(reset)

        while guesses != 0:
            color_print("Choose a letter : ", yellow)
            choice = (str(input()))

            for index, letter in enumerate(hangman):

                if choice == "":
                    color_print("Invalid Response", red)
                    break

                elif choice in letter:
                    color_print("Correct!", yellow)
                    answer[index] = choice
                    answer_output = separator.join(answer)
                    color_print(answer_output, cyan, bold)
                    print()
                    if answer_output == hangman:
                        color_print("Congratulations You've won!", bold, yellow)
                        control = 1

                        while control == 1:
                            color_print("Press 0 to end, or 1 to play again",yellow)
                            again = input()

                            if again == '0':
                                control = 3
                                guesses = 0
                                break
                            elif again == '1':
                                guesses = 0
                                control = None
                                break
                            else:
                                color_print("Invalid input, try again: ", red)
                                pass

                elif choice not in hangman:
                    print(red)
                    print("Wrong!")
                    guesses -= 1
                    print("You only have ", guesses, " guesses left!")
                    print(reset)
                    break

            if guesses == 0 and control == 1:
                print(red)
                print("Unfortunately, you've been hung")
                print()
                print(yellow)
                print("\nThe answer was ", word,
                      "\n"
                      "\nBetter luck next time")
                print(reset)

                while control == 1:
                    print()
                    print("Press 0 to end, or 1 to play again")
                    again = input()

                    if again == '0':
                        control = 3
                        guesses = 0
                        break
                    elif again == '1':
                        guesses = 0
                        control = None
                        break
                    else:
                        color_print("Invalid input, try again: ", red)
                        pass

        if control == 3:
            break

hangman_game()