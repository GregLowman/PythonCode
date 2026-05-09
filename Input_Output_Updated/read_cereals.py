"""Read cereal grain nutritional data from CSV and let the user look up grains interactively."""
import csv
csv_filename = 'cereal_grains.csv'
grain_dict = {}

with open(csv_filename, encoding='utf-8', newline='') as csv_file:
    reader = csv.reader(csv_file, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        cereal, calories, fats, proteins, fiber, vitamin_e = row
        grain_dict.setdefault(cereal, (calories, fats, proteins, fiber, vitamin_e))
        print(cereal)

    print("Type Q to Quit")
    while True:
        csv_file.seek(0)
        choice = input("Select a Cereal Grain: ")
        if choice in grain_dict.keys():
            calories, fats, proteins, fiber, vitamin_e = grain_dict[choice]
            print(f"In {choice}:"
                  f" \n\tCalories: {calories}"
                  f"\n\tFats: {fats}"
                  f"\n\tProteins: {proteins}"
                  f"\n\tFiber: {fiber}"
                  f"\n\tVitamin E: {vitamin_e}")
            pass

        elif choice == 'Q'.casefold():
            break
        else:
            print("Input a Valid Cereal")
            pass
