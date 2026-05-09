"""Categorise creatures into biting, stinging, arachnid, and non-arachnid sets."""
scorpions = {"emperor", "red claw", "arizona", "forest", "fat tail"}
snakes = {"python", "cobra", "viper", "anaconda", "mamba"}
spiders = {"tarantula", "black widow", "wolf spider", "crab spider"}
vespas = {"yellowjacket", "hornet", "paper wasp"}

what_bites = set(snakes.union(spiders))
what_stings = set(scorpions | vespas)

arachnids = set()
non_arachnids = set()

arachnids.update(scorpions, spiders)
non_arachnids |= snakes
non_arachnids |= vespas

print("This is a list of what bites: ", sorted(what_bites), sep="::")
print()
print(f"This is a list of what stings: {sorted(what_stings)}", sep="::")
print()

print("This is a list of arachnids: ", sorted(arachnids))
print()
print("This is a list of non-arachnids: ", sorted(non_arachnids))