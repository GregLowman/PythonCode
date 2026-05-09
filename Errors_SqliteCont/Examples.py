"""Demonstrates exception handling with try/except for RecursionError and ZeroDivisionError."""


def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


try:
    print(factorial(998))
except (RecursionError, ZeroDivisionError):
    print("This program cannot calculate, factorials too large")
print("Program terminating")
