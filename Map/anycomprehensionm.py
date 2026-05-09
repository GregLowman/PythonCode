"""Use any() and all() with namedtuple plant data and a people list to check completeness."""
from data import people, plants_list, plants_dict

if bool(people) and all([person[1] for person in people]):
    print("Sending email")
else:
    print("User must edit the list of recipients")

if any([plant.plant_type == "Grass" for plant in plants_list]):
    print("This pack contains grass")
else:
    print("No grasses in this pack")


if any(plant.plant_type == "Grass" for plant in plants_dict.values()):
    print("This dict contains grasses")

else:
    print("No grasses in the dict")

