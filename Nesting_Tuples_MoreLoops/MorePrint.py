"""Show how wrapping print arguments in parentheses creates a tuple rather than separate values."""
name = "Tim"
age = 10

print(name, age, "Python", 2020)
print((name, age, "Python", 2020))
