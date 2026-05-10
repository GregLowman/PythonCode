"""Show the all() gotcha: all([]) returns True on an empty iterable; guard with bool() check."""
entries = []

if entries:
    print(f"All: {all(entries)}")
else:
    print(False)
print(f"Any: {any(entries)}")

result = bool(entries) and all(entries)
print(result)
