"""Join a list of flower names into a single string with a pipe separator using str.join()."""
flowers = [
    "Daffodil",
    "Evening Primrose",
    "Hydrangea",
    "Iris",
    "Lavender",
    "Sunflower",
    "Tiger Lily",
]

separator = " | "
output = separator.join(flowers)
print(output)