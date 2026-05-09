"""Demonstrate the 'not in' operator by checking whether user input mentions the cinema."""
activity = input("What would you like to do today? ")

if "cinema" not in activity.casefold():
    print("But I want to go to the cinema")
