"""Demonstrates unpacking a tuple into *args using a variadic test function."""
numbers = (0, 1, 2, 3, 4, 5)


def test_star(*args):
    print(args)
    for x in args:
        print(x)


test_star(0, 1, 2, 3, 4, 5)

print()
test_star()
