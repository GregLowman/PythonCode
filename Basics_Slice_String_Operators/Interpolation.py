"""Demonstrates Python 2-style % string interpolation (for historical reference)."""
age = 24
print("My age is %d years" % age)

major = "years"
minor = "months"
print("My age is %d %s, %d %s" % (age, major, 6, minor))
print("PI is approximately %f" % (22/7))
print("PI is approximately %60.50f" % (22/7))

print("DO NOT USE IN PYTHON 3")
