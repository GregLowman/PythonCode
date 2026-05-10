"""timeit comparison of iterative vs recursive factorial: timing, mean, and standard deviation."""
import timeit
from statistics import mean, stdev

number = 100
amount = 10000


def fact(n=number):
    result = 1
    if n > 1:
        for f in range(2, n+1):
            result *= f
    return result


def factorial(n=number):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


if __name__ == "__main__":
    iterative = timeit.repeat(fact, number=amount)
    recursive = timeit.repeat(factorial, number=amount)

    print(f"Amount of time for Iterative: {iterative}")
    print(f"Amount of time for Recursive: {recursive}")

    print()

    print(f"Sum of iterative function {sum(iterative)}")
    print(f"Sum of recursive function {sum(recursive)}")

    print()

    print(f"Mean of iterative is {mean(iterative)}")
    print(f"Mean of recursive is {mean(recursive)}")

    print()

    print(f"Standard Deviation of iterative is {stdev(iterative)}")
    print(f"Standard Deviation of recursive is {stdev(recursive)}")
