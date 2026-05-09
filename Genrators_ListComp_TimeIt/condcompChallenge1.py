"""FizzBuzz as a single list comprehension using chained ternary expressions."""
fizzbuzz = ["fizzbuzz" if number % 15 == 0 else
            "fizz" if number % 3 == 0 else
            "buzz" if number % 5 == 0 else
            number for number in range(1, 31)]

print(fizzbuzz)
