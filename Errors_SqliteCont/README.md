# Errors and SQLite Continued

Exception handling patterns and SQLite database operations including parameterized queries.

## Files

| File | Topic |
|---|---|
| `Examples.py` | try/except for `RecursionError` and `ZeroDivisionError` in a recursive factorial |
| `Errors Challenge.py` | Division loop with try/except/finally covering multiple exception types and `sys.exit` |
| `contacts.py` | Creates a contacts table, inserts rows, and demonstrates `fetchone()` and cursor iteration |
| `contacts2.py` | Updates a contact's email using parameterized `?` queries to prevent SQL injection |
| `challenge.py` | Inserts and retrieves a contact from SQLite using user input |

## Key Concepts
- `try/except/finally` and catching multiple exception types in one clause
- `RecursionError` from deep recursive calls
- SQLite CRUD operations with `sqlite3`
- Parameterized queries (`?` placeholders) vs. string formatting in SQL
- `cursor.fetchone()` vs. iterating directly over a cursor
