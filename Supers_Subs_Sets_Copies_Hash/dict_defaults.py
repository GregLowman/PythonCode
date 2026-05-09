"""Demonstrate setdefault and get for safe pantry lookups."""
from contents import pantry

chicken_quantity = pantry.setdefault("chicken", 0)
print(f"Chicken: {chicken_quantity}")

bean_quantity = pantry.setdefault("beans", 0)
print(f"Beans: {bean_quantity}")

ketchup_quantity = pantry.get("ketchup", 0)
print(f"Ketchup: {ketchup_quantity}")

z_quantity = pantry.setdefault("zucchini", "eight")
print(f"zucchini: {z_quantity}")

print()
print("Pantry now contains...")

for key, value in sorted(pantry.items()):
    print(key, value)
