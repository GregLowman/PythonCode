"""Show enumerate() returning (index, value) tuples, and how to unpack them manually."""
for t in enumerate("abcdefgh"):
    index, character = t
    print(t)

index, character = (0, 'a')
print(index)
print(character)
