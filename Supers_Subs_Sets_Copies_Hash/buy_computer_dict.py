"""Computer part picker: select parts from a numbered menu until done."""
available_parts = {"1": "Computer",
                   "2": "Monitor",
                   "3": "Keyboard",
                   "4": "Mouse",
                   "5": "HDMI Cable",
                   "6": "DVD Drive",
                   }


current_choice = None
while current_choice != "0":
    if current_choice in available_parts:
        chosen_part = available_parts[current_choice]
        print(f"Adding {chosen_part}")
    else:
        print("Please ass options from the list")
        for num, item in available_parts.items():
            print(num, item, sep=" | | ")
        print("0: to finish")

    current_choice = input("> ")
