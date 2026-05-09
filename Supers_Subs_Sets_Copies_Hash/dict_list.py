"""Toggle computer parts in/out of a shopping list using a shared dict."""
available_parts = {"1": "Computer",
                   "2": "Monitor",
                   "3": "Keyboard",
                   "4": "Mouse",
                   "5": "HDMI Cable",
                   "6": "DVD Drive",
                   }
shopping_list = {

}

current_choice = None
while current_choice != "0":
    if current_choice in available_parts:
        if current_choice in shopping_list:
            print(f"Removing {current_choice} from shopping list")
            del shopping_list[current_choice]
        else:
            chosen_part = available_parts[current_choice]
            print(f"Adding {chosen_part} to Shopping List")
            shopping_list[current_choice] = available_parts[current_choice]
    else:
        print("Please ass options from the list")
        for num, item in available_parts.items():
            print(num, item, sep=" | | ")
        print("0: to finish")

    current_choice = input("> ")

print(f"Available parts includes {available_parts.items()}")
print(f"Shopping list includes {shopping_list.items()}")
