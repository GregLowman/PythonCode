"""Read and display fields from a shelve-backed motorcycle record."""
import shelve

with shelve.open("bike2") as bike:
    for key in bike:
        print(key)

    print("=" * 40)

    print(bike["engine_size"])
    print(bike["color"])
