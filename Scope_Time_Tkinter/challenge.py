"""Timed math-problem game: random arithmetic challenges with reaction-time scoring."""
import time
import random

print("Solve the problem as soon as possible: ")
operate = ['+', '-', 'x', '%']
answer = 0

while True:
    operate_choice = random.choice(operate)

    if '-' in operate_choice or '+' in operate_choice:
        variable1 = random.randint(1, 1000)
        variable2 = random.randint(1, 1000)
    else:
        variable1 = random.randint(1, 100)
        variable2 = random.randint(1, 20)

    input("Press Enter to Begin")
    start_time = time.time()

    print(variable1, operate_choice, variable2)

    if operate_choice == '+':
        answer = variable1 + variable2
    elif operate_choice == '-':
        answer = variable1 - variable2
    elif operate_choice == 'x':
        answer = variable1 * variable2
    elif operate_choice == '%':
        answer = variable1 / variable2

    guess = int(input("Answer: "))
    end_time = time.time()
    total_time = end_time - start_time

    if guess == answer:
        print("Correct")
        print("It took you {} seconds to get the answer!".format(total_time))
    elif guess != answer:
        print("Incorrect")
        print("The answer was {}".format(answer))
        print("You took a total of {} seconds to answer".format(total_time))
    else:
        print("Excuse me, how did you manage this")

    print("Would you like to try again?")

    while True:
        choice = int(input("Press 1 to play again or 0 to quit >> "))

        if choice == 1:
            break
        elif choice == 0:
            break
        else:
            pass
    if choice == 0:
        break
