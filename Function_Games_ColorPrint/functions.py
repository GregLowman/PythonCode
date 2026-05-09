"""Function examples: multiply, palindrome checking, and iterative Fibonacci."""


def multiply(x: float, y: float) -> float:
    """
    Takes two numbers and multiplies them.

    Two numbers are input by the user, and then those numbers are multiplied and returned.

    :param x: User input of the first number.
    :param y: User input of the second number.
    :return: Returns the product of `x` times `y`
    """
    result = x * y
    return result


def is_palindrome(string: str) -> bool:
    """
    Check to see if given word is a palindrome

    Function will run once and return a boolean value,
    letting us know if the word is the same word backwards.

    :param string: The word that the user has previously input.
    :return: Returns True or False, determining whether it is a palindrome or not
    """
    return string[::-1].casefold() == string.casefold()


def palindrome_sentence(string: str) -> bool:
    """
    Checks to see if a sentence is a palindrome or not

    Function will run a loop to determine if the given sentence is a palindrome or not.
    Once the loop has gone through the entire sentence, the function will return and end.

    :param string: The sentence that the user has previously input.
    :return: Returns a True or False, boolean statement, regarding whether or not
        the sentence is the same backwards (palindrome)
    """
    forward = ""
    for char in string:
        if char.isalnum():
            forward += char
    return is_palindrome(forward)


def fibonacci(n: int) -> int:
    """Return the `n` th Fibonacci number, for positive `n` ."""
    if 0 <= n <= 1:
        return n

    n_minus1, n_minus2 = 1, 0

    result = None
    for f in range(n - 1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result

    return result


for i in range(36):
    print(i, fibonacci(i))

word = input("Please enter a word or sentence to check: ")
if palindrome_sentence(word):
    print("'{}' is a palindrome".format(word))
else:
    print("'{}' is not a palindrome".format(word))
