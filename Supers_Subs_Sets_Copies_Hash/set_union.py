"""Collect all drugs involved in adverse interactions using set union and update."""
from prescription_data import adverse_interactions

med_to_watch = set()

med_to_watch.update(*adverse_interactions)
print(*sorted(med_to_watch), sep="\n")
