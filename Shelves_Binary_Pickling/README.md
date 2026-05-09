# Shelves, Binary & Pickling

Python scripts demonstrating file I/O from plain text through binary, `pickle`, and `shelve` persistence.

## Files

| File | Description |
|---|---|
| `file.io.py` | Read a text file as a single string; print it forward and reversed |
| `writing.py` | Serialize a tuple to a text file using `print`/`eval`, then read it back |
| `challenge.py` | Append formatted multiplication tables (2–12) to a text file |
| `binary.py` | Write and read binary data with big/little-endian integer encoding |
| `pickling.py` | Pickle multiple objects into one file and load them back in order |
| `motorcycle.py` | Read fields from a shelve-backed motorcycle record |
| `Shelve.example.py` | Populate a shelve with fruit descriptions and iterate values/items |
| `recipes_example.py` | Update a shelve-backed recipe store using `writeback` mode |
| `example.py` | Store nested dicts in a shelve and retrieve by nested key |
| `shelve_challenge.py` | In-memory cave adventure: navigate locations with a vocabulary map |
| `cave_initialise.py` | Seed shelve databases for the cave game (locations + vocabulary) |
| `cave_game.py` | Cave adventure loading state from shelve; navigate by typed commands |

## Concepts

- **File I/O**: `open`, `read`, `readline`, `readlines`, `write`, append mode
- **Binary files**: `bytes`, `to_bytes`, `from_bytes`, big/little-endian
- **Pickle**: `pickle.dump`, `pickle.load`, multiple objects, protocol levels
- **Shelve**: `shelve.open`, `writeback`, `sync`, nested data, key iteration
