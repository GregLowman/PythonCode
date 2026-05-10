"""Access and replace namedtuple fields on a Plant list, showing attribute access vs index."""
from data import plants_list

print(plants_list[0])

for plant in plants_list:
    print(plant.name)
    print(plant.scientific_name)

print()

example = plants_list[0]
print(example)
example = example._replace(lifecycle='Annual')
print(example)