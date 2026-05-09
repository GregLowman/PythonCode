# Object-Oriented Programming — Classes

Introduction to OOP in Python: class definitions, instance vs class attributes, methods, and a multi-class music library application.

## Files

| File | Description |
|------|-------------|
| `Oop.py` | Introduce classes: `Kettle` with instance and class attributes, instance methods, and `__dict__` inspection |
| `accounts.py` | `Account` class with pytz-timestamped transaction history; deposit, withdraw, and show_transactions |
| `song.py` | `Song`, `Album`, and `Artist` classes; reads `albums.txt` and writes `checkfile.txt` |
| `Oop Challenge.py` | Challenge version of song.py — simplified `Artist` stores artist name as a plain string |

## Assets Required

- `albums.txt` — tab-delimited file with columns: `artist`, `album`, `year`, `song`

## Key Concepts

- **Class vs instance attributes**: Class attributes are shared across all instances; instance attributes are per-object.
- **`__init__`**: Constructor method that initialises instance state.
- **Methods**: Functions defined inside a class that operate on `self`.
- **`@staticmethod`**: Method that belongs to the class but receives no implicit `self` or `cls` argument.
- **`property()`**: Expose a method as an attribute accessor.
- **`__dict__`**: Inspect the instance or class namespace at runtime.
- **`pytz`**: Timezone-aware datetime handling with `utc.localize()` and `astimezone()`.

## Dependencies

```
pip install pytz
```
