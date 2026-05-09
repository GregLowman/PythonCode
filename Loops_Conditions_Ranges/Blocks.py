"""Demonstrate if/elif/else blocks with an age-based voting eligibility check."""
name = input("Please enter your name:")
age = int(input("How old are you, {0}? ".format(name)))
print()
if age >= 18:
    print("You're old enough to vote")
    print("Please put an X in the box")
elif age == 0:
    print("Far too young")
else:
    print("Please come back in {0} years".format(18 - age))

