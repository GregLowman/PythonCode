"""Demonstrates *args for variadic positional parameters using a sum function."""


def sum_numbers(*numbers: float) -> float:
    """
    Takes given input numbers, adds them all, and outputs a sum.

    :param numbers: User input numbers.
    :return: A float containing the sum of the numbers.
    """
    sum_of = 0
    for num in numbers:
        sum_of += num
    return sum_of


print(sum_numbers(1, 2, 3))
print(sum_numbers(8, 20, 2))
print(sum_numbers(12.5, 3.147, 98.1))
print(sum_numbers(1.1, 2.2, 5.5))
