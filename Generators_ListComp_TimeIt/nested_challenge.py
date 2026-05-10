"""timeit comparison: nested list comprehension vs generator expression for multiplication pairs."""
import timeit

number = 100000
the_range = range(1, 11)


def first():
    for product in [[(x, x * y) for x in the_range] for y in the_range]:
        return product


def second():
    for a, b in ((x, x * y) for x in the_range for y in the_range):
        return a, b


test_one = timeit.timeit(first, number=number)
test_two = timeit.timeit(second, number=number)

print(f"Test one took {test_one}")
print(f"Test two took {test_two}")
