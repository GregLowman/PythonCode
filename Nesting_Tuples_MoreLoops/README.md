# Nesting, Tuples, and More Loops

Exercises covering Python lists, tuples, nested data structures, mutability, iteration patterns, and string manipulation methods.

## Files

| File | Description |
|------|-------------|
| `ListsIntro.py` | List creation, indexing, slicing, and slice assignment |
| `Mutable.py` | List mutability: multiple variables pointing to the same list all reflect mutations |
| `immutable.py` | String immutability: augmenting a string creates a new object with a different id |
| `TuplesIntro.py` | Tuples as immutable records; unpacking in a for loop |
| `Unpacking.py` | Multiple assignment and tuple/list unpacking into named variables |
| `MorePrint.py` | How parentheses around print arguments create a tuple instead of separate values |
| `NumberLists.py` | Nested list of even/odd numbers; iterating with inner and outer loops |
| `Sorted.py` | `sorted()` and `list.sort()` on characters, numbers, and case-insensitive names |
| `GoBackwards.py` | Delete out-of-range values by iterating in reverse with `enumerate(reversed())` |
| `Outliers.py` | Remove leading and trailing outliers from a sorted list using slice deletion |
| `EnumerateExample.py` | `enumerate()` returning `(index, value)` tuples; manual unpacking |
| `JoiningThings.py` | `str.join()` to combine a list into a single delimited string |
| `SplittingThings.py` | `str.split()` on whitespace and a delimiter; converting split values to integers |
| `spam.py` | Count spam occurrences per meal; print items for spam-free meals |
| `NoSpam.py` | Remove all spam items from meals using a `while` loop |
| `BuyComputer.py` | Interactive part selector: toggle items in/out of a basket by number |
| `Demo.py` | Nested data structure: albums as tuples containing a track list |
| `NestedData.py` | Shared album data module used by `JukeboxMenu` |
| `JukeboxMenu.py` | Interactive jukebox: pick an album then a song from nested tuple data |
| `Testing.py` | Build album/artist/year display strings from a tuple of album records |
| `Random_Word.py` | Pick a random word of 5–8 letters from predefined word lists |
| `HangmanPtTwo.py` | Hangman game with ANSI colour output: 6 guesses to identify a random word |

## Key Concepts

- **Lists vs tuples**: Lists are mutable; tuples are immutable records.
- **Mutability and identity**: `id()` reveals when two names point to the same object.
- **Nested data**: Lists of tuples, tuples containing lists — mixing structures for real-world data.
- **Iteration patterns**: `enumerate()`, `reversed()`, `range(len(...), -1, -1)` for index-safe deletion.
- **`sorted()` / `list.sort()`**: The `key=` argument (e.g. `str.casefold`) enables case-insensitive ordering.
- **String methods**: `str.join()`, `str.split()`, `str.strip()`.
- **ANSI escape codes**: Inline terminal colour formatting without third-party libraries.

## Dependencies

`HangmanPtTwo.py` imports `colorama` (though not used directly — `colorama` is imported but ANSI codes are applied manually). Install with:

```
pip install colorama
```
