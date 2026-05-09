"""Filter a list of numbers, flagging any that are divisible by 8."""
numbers = [1, 45, 32, 12, 60]

for number in numbers:
    if number % 8 == 0:
        print("{} is unacceptable".format(number))
    else:
        print("{} is an ok number".format(number))
