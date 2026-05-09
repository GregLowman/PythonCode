"""Update a shelve-backed recipe store using writeback mode."""
import shelve

soup = ["tin of soup"]

with shelve.open('recipes', writeback=True) as recipes:
    recipes['soup'] = soup
    recipes.sync()
    soup.append("cream")

    for snack in recipes:
        print(snack, recipes[snack])
