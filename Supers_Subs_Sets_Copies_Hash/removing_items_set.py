"""Remove specific integers from a set using discard (safe) and remove (raises on miss)."""
small_ints = set(range(21))
print(small_ints)

small_ints.discard(10)
small_ints.remove(11)
print(small_ints)

small_ints.discard(99)
print(small_ints)
