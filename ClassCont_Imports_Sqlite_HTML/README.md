# Classes Continued — Imports, SQLite, and HTML

Intermediate Python exercises covering class design patterns, module imports, SQLite persistence, and programmatic HTML generation.

## Files

| File | Topic |
|---|---|
| `ducks.py` | Duck typing and composition — Wing ratio determines flight; Flock uses `getattr` instead of `isinstance` |
| `Migration.py` | Imports `ducks` module and runs a Flock migration |
| `enemy.py` | Enemy class hierarchy: Troll, Vampire (dodge), VampireKing (reduced damage + dodge) |
| `player.py` | Player with property-based lives/level; score adjusts automatically with level changes |
| `html_doc.py` | HTML document builder via Tag composition — writes well-formed HTML to a file |
| `rollback.py` | SQLite bank account with `try/except/else` rollback on failed transactions |
| `rollback2.py` | Bank account using `Decimal` to avoid floating-point precision errors |
| `tztest.py` | SQLite account with timezone-aware timestamps stored using `pickle` |
| `checkdb.py` | Queries the `localhistory` view and prints all rows |
| `txcheck.py` | Reads raw history rows and converts UTC timestamps to local time |
| `main.py` | Demonstrates `print()` keyword arguments: `sep` and `end` |

## Assets
- `accounts.sqlite` — SQLite database used by rollback, tztest, checkdb, and txcheck

## Key Concepts
- Duck typing with `getattr` and `callable()` over `isinstance`
- Python `property` decorator for validated attribute access
- SQLite with `detect_types` for automatic timestamp conversion
- `try/except/else` for transaction rollback
- `Decimal` for precise financial arithmetic
- Programmatic HTML generation via class composition

## Dependencies
```
pip install pytz
```
