"""Interactive shopping list: add or remove computer parts by number; toggle items in/out of a basket."""
available_parts = ["Computer",
                   "Monitor",
                   "Keyboard",
                   "Mouse",
                   "HDMI Cable",
                   "DVD Drive"
                   ]
current_choice = "-"
valid_choices = []
for i in range(1, len(available_parts) + 1):
    valid_choices.append(str(i))
print(valid_choices)
computer_parts = []

while current_choice != '0':
    if current_choice in valid_choices:
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        if chosen_part in computer_parts:
            print("Removing {}".format(current_choice))
            computer_parts.remove(chosen_part)
        else:
            print("Adding {}".format(current_choice))
            computer_parts.append(chosen_part)
        print("Your list now contains: {}".format(computer_parts))
    else:
        print("Please add options from the list below:")
        for number, part in enumerate(available_parts):
            print("{0}: {1}".format(number + 1, part))

    current_choice = input("Enter: ")

print(computer_parts)
