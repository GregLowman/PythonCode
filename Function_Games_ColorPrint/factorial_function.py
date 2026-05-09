"""Iterative factorial implementation printed for a range of values."""


def factorial_function(number: int) -> int:
    """
    Determines the factorial of any given number

    :param number: Number given from previous input
    :return: Returns factorial as integer
    """
    factorial = 1
    if number == 0:
        return 1
    else:
        for num in range(1, number + 1):
            factorial *= num
        return factorial


MAX = 36
MIN = 0

for digit in range(MIN, MAX):
    print(digit, "||", factorial_function(digit))
