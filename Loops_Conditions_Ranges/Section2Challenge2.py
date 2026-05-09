"""Challenge: guessing game with user-defined range, guess counter, and 0 to quit."""
import random

highest = int(input("How high should the numbers be? "))
answer = random.randint(1, highest)
guess = 0
counter = 0
print("Input 0 to quit")
print("")
print("Guess a number between 1 - {} : ".format(highest))
while guess != answer:
    guess = int(input())

    print("-" * 80)

    if guess > answer:
        if guess != 0:
            print("Sorry, guess lower: ")
            counter += 1
        elif guess == 0:
            print("Game over, player quits")
            break
    elif guess < answer:
        if guess != 0:
            print("Sorry, guess higher: ")
            counter += 1
        elif guess == 0:
            print("Game over, player quits")
            break
    else:
        print("Correct! Congratulations")
        counter += 1
        print("It only took {} guesses!".format(counter))
        break
    if guess == 0:
        print("Game over, player quits")
        break
