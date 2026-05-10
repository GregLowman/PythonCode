"""List comprehension challenge: word lengths and (word, length) tuples from user input."""
text = input("Please enter your text: ")

output = []
for x in text.split():
    output.append(len(x))
print(output)

output_answer = [len(word) for word in text.split()]
print(output_answer)

output = []
for x in text.split():
    output.append((x, len(x)))
print(output)

output_answer2 = [(word, len(word)) for word in text.split()]
print(output_answer2)
