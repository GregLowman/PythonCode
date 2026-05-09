# Supers, Subs, Sets, Copies & Hash

Python scripts covering dictionaries, sets, shallow/deep copies, and hashing.

## Files

| File | Description |
|---|---|
| `zen.py` | Print the Zen of Python |
| `dict_intro.py` | Dict mutation: add, update, delete, and pop with defaults |
| `buy_computer_dict.py` | Part picker: select from a numbered menu until done |
| `dict_list.py` | Toggle parts in/out of a shopping list using a shared dict |
| `recipe_options.py` | Compare list-of-tuples vs nested-dict recipe layouts |
| `meal_planner.py` | Pick a recipe, check pantry stock, build a shopping list |
| `dict_defaults.py` | Safe pantry lookups using `setdefault` and `get` |
| `challenge.py` | Count alphanumeric character frequencies with a dict |
| `dict_methods.py` | Dict views: `values()`, `keys()`, `items()`, reverse-key lookup |
| `shallow_copy_2.py` | Show that a shallow copy shares inner list objects with the original |
| `shallow_copy.py` | Show that `deepcopy` produces fully independent inner lists |
| `deepcopy_is_recursive.py` | Verify deepcopy is recursive: original changes don't propagate |
| `copy_challenge.py` | Custom shallow-copy for dicts whose values are lists or dicts |
| `atrocious_hash.py` | Trivial first-char-ordinal hash and its collision behaviour |
| `secure_hash.py` | Detect code tampering using SHA-256 (`hashlib`) |
| `set_intro.py` | Sets: ordering, equality, and why index access is unsupported |
| `summarychallenge.py` | Choice menu using a set for O(1) membership testing |
| `modifying_sets.py` | Add items to a set; deduplicate a list while preserving order |
| `removing_items_set.py` | `discard` (safe) vs `remove` (raises on miss) |
| `prescription_data.py` | Drug and patient prescription data shared by prescription modules |
| `prescription_trial.py` | Switch trial patients from Warfarin to Edoxaban |
| `prescription_processing.py` | Pop patients off the trial set and print prescriptions |
| `practice_with_sets.py` | Categorise creatures: biting, stinging, arachnid, non-arachnid |
| `set_union.py` | Collect all drugs in adverse interactions using union/update |
| `primes_and_squares.py` | Generate primes (Sieve of Eratosthenes) and squares via generators |
| `set_intersection.py` | Intersection of even/odd and prime/square number sets |
| `set_difference.py` | Set difference: odd non-primes and prime non-odds |
| `trial_patients.py` | Three-way set intersection to find potential animal mounts |
| `packing_list.py` | Remove plane-restricted items from a packing list |
| `set_sd.py` | Symmetric difference: courses unique to morning or afternoon |
| `super_sub.py` | Subset, superset, and proper-subset operators on animal sets |
| `candidates.py` | Filter candidates whose skills are a superset of requirements |
| `contents.py` | Shared pantry inventory and recipes data module |

## Concepts

- **Dicts**: mutation, `pop`, `setdefault`, `get`, views, `fromkeys`, `update`
- **Copies**: `dict.copy()` (shallow), `copy.deepcopy()`, custom deep-copy
- **Hashing**: simple ordinal hash, SHA-256 with `hashlib`
- **Sets**: creation, `add`/`discard`/`remove`, union, intersection, difference, symmetric difference, subset/superset operators
