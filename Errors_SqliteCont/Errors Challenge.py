"""Division challenge demonstrating try/except/finally with multiple exception types and sys.exit."""
import sys


def divide():
    """Simple division function"""
    x = int(input("Give a value for x: "))
    y = int(input("Give a value for y: "))
    z = x / y

    print(z)


def error():
    """Crash prevention"""
    print('Sorry, an error has occurred, try again.')


control = True

while control:
    try:
        divide()
        control = False
        sys.exit(1)
    except (ValueError, ZeroDivisionError, RecursionError, OverflowError):
        error()
    except EOFError:
        sys.exit("Hey, don't do that")
    finally:
        print("The program has successfully worked")

