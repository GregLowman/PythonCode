"""Show that strings are immutable: augmenting a string creates a new object with a different id."""
result = "Correct"
another_result = result
print(id(result))
print(id(another_result))

result += "ish"
print(id(result))
