"""Final challenge: menu-driven activity selector that loops until the user exits."""
selection = 10

while selection != 0:

    print("Choose an option from the list below: ")
    print("1.\t Learn Python")
    print("2.\t Learn Java")
    print("3.\t Go Swimming")
    print("4.\t Have dinner")
    print("5.\t Go to bed")
    print("0.\t Exit")
    print("-" * 80)

    selection = int(input())

    if selection == 1:
        print("You chose: \n \t Learn Python")
        print("*" * 80)
        print()
        continue
    elif selection == 2:
        print("You chose: \n \t Learn Java")
        print("*" * 80)
        print()
        continue
    elif selection == 3:
        print("You chose: \n \t Go Swimming")
        print("*" * 80)
        print()
        continue
    elif selection == 4:
        print("You chose: \n \t Have Dinner")
        print("*" * 80)
        print()
        continue
    elif selection == 5:
        print("You chose: \n \t Go to bed")
        print("*" * 80)
        print()
        continue
    elif selection == 0:
        break
    else:
        print("Please input a valid option")
        print("*" * 80)
        print()