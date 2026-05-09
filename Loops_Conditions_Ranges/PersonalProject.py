"""Personal project: a letter-by-letter hangman game for the word 'python'."""
hangman = "python"
answer = ""
number = 2
guess = ""
wrong = ""
control = 6

for char in hangman:
    number = number + control
    while number != 0:

        guess = input("Please guess a letter:  ")

        if guess == char:
            answer = answer + guess
            print("You got one!")
            print(answer)
            guess = ""
            number = 0
        elif guess != char:
            number = number - 1
            control = control - 1
            print("Incorrect, only {} attempts left".format(number))
            print("-" * 80)
            print()
            print(answer)
            guess = ""
            wrong = char
            if number == 1:
                print("Only one chance left, make it count")
            if number == 0:
                print("Sorry, you've been hung")
                guess = wrong
                char = hangman

            while guess != wrong:
                guess = input("Please guess a letter:  ")

                if guess == wrong:
                    print("Nice!")
                    answer = answer + guess
                    print(answer)
                    number = 0
                else:
                    number = number - 1
                    control = control - 1
                    print("Incorrect, only {} attempts left".format(number))
                    print("-" * 80)
                    print()
                    print(answer)
                    guess = ""
                    if number == 1:
                        print("Only one chance left, make it count")
                    if number == 0:
                        print("Sorry, you've been hung")
                        guess = wrong
                        char = hangman


if answer == hangman:
    print("Congratulations you won!")