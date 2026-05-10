"""Squares a range using a list comprehension — direct comparison to listfor.py."""
print(__file__)

numbers = [num for num in range(1, 100)]

number = int(input("Please enter a number, and I'll tell you its square: "))

squares = [number ** 2 for number in numbers]

index_pos = numbers.index(number)
print(squares[index_pos])