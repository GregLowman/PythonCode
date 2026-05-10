"""timeit benchmark comparing list comprehension vs map() for capitalising characters and words."""
import timeit

number = 10000000
times = 5
text = "what have the romans ever done for us"


def capital_letters():
    capitals = [char.upper() for char in text]
    return capitals


def map_capital_letters():
    map_capitals = list(map(str.upper, text))
    return map_capitals


def capital_word():
    words = [word.upper() for word in text.split(' ')]
    return words


def map_capital_word():
    map_words = list(map(str.upper, text.split(' ')))
    return map_words


time_capitalLetters = timeit.repeat(capital_letters, number=number, repeat=times)
time_mapCapLet = timeit.repeat(map_capital_letters, number=number, repeat=times)
time_capWord = timeit.repeat(capital_word, number=number, repeat=times)
time_mapCapWord = timeit.repeat(map_capital_word, number=number, repeat=times)

print(f"All times are an average of {times} times")
print(f"Capital letters not using Map: {((sum(time_capitalLetters)) / times)}")
print(f"Capital letters using Map: {((sum(time_mapCapLet)) / times)}")
print(f"Capital words not using Map: {((sum(time_capWord)) / times)}")
print(f"Capital words using Map: {((sum(time_mapCapWord)) / times)}")
