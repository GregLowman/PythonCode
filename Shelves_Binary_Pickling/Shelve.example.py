"""Open a shelve, populate it with fruit descriptions, and iterate its values and items."""
import shelve

fruit = shelve.open('ShelfTest')
fruit['orange'] = "a sweet, orange, citrus fruit"
fruit['apple'] = "good for making cider"
fruit['lemon'] = "sour, yellow, citrus fruit"
fruit['grape'] = "a small sweet fruit growing in bunches"
fruit['lime'] = "a sour, green citrus fruit"

for v in fruit.values():
    print(v)

print(fruit.values())

for f in fruit.items():
    print(f)

print(fruit.items())

fruit.close()
