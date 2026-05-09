"""Bubble sort implementation with pass-by-pass output and comparison counting."""


def bubble_sort(data: list) -> None:
    """Sorts a list in place."""
    n = len(data)
    comparison_count = 0

    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            comparison_count += 1
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                swapped = True

        print(f"End of pass {i}. 'data' is now {data}")
        if not swapped:
            print("List is now sorted")
            break
    print(f"comparison_count is {comparison_count}")


numbers = [7, 6, 5, 4, 3, 2, 1]
print(len(numbers))
print(f"Sorting {numbers}")
bubble_sort(numbers)
print(f"The sorted data is {numbers}")
