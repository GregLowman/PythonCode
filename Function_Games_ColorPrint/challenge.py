"""FizzBuzz game — computer prints even turns, player types the answer for odd turns."""


def fizz_buzz(num: int) -> str:
    """
    This function returns a predetermined response depending on the number.

    If the number is divisible by 3 it returns `fizz`, if the number
    is divisible by 5 it returns `buzz`, and if the number is divisible
    by both it will return `fizzbuzz`, however if it is none of the above,
    it will simply return the number.

    :param num: Input of number to be determined.
    :return: Returns either `fizz`, `buzz`, `fizzbuzz`, or the original number.
    """
    if (num % 3 == 0) and (num % 5 == 0):
        return "fizz buzz"
    elif num % 3 == 0:
        return "fizz"
    elif num % 5 == 0:
        return "buzz"
    else:
        return str(num)


def answer_check(check: str) -> bool:
    """
    Function checks if answer is correct

    :param check: answer input from user
    :return: boolean true or false
    """
    if answer == fizz_buzz(number):
        print("Correct")
        return True
    else:
        print("Incorrect: Game over")
        return False


HIGH = 101
LOW = 1
answer = None

print("Get ready to play Fizz Buzz")
print("Type Fizz if divisible by 3")
print("Type Buzz if divisible by 5")
print("Type Fizz Buzz if divisible by both")
print("Type the number if none of the above")
print()
print("*" * 80)

for number in range(LOW, HIGH):
    if number in range(LOW + 1, HIGH, 2):
        answer = str(input("Type Here: ")).casefold()
        if answer_check(answer):
            pass
        else:
            break

    elif number in range(LOW, HIGH, 2):
        print(fizz_buzz(number))

    elif number == 100:
        print("Congratulations you've won!")
