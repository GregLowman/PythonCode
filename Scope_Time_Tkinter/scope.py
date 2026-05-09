"""Compare iterative and recursive implementations of factorial and Fibonacci."""


def fact(n):
    """ Calculate n! iteratively """
    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
    return result


def factorial(n):
    """ Calculates n! recursively"""
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


def fib(n):
    """F(n) = F(n-1) + F(n-2)"""
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)


def fibonacci(n):
    """Calculate the nth Fibonacci number iteratively."""
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        n_minus1 = 1
        n_minus2 = 0
        for f in range(1, n):
            result = n_minus2 + n_minus1
            n_minus2 = n_minus1
            n_minus1 = result
    return result


for i in range(2000000):
    print(i, fibonacci(i))

