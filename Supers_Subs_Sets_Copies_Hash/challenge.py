"""Count alphanumeric character frequencies in a string using a dict."""
word_count = {}


def char_checker(let):
    if let.isalnum():
        word_count[let] = word_count.setdefault(let, 0) + 1
        return let
    else:
        return None


text = "Later in the course, you'll see how to use the collections Counter class."

for char in text.casefold():
    char_checker(char)
for letter, count in sorted(word_count.items()):
    print(letter, count)
