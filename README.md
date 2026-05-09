# Python Code

A collection of exercises and projects worked through while learning Python from the ground up. Sections follow the course progression from core syntax through advanced topics, with each folder focused on a specific language feature or concept area.

## Sections

### Foundations
| Section | Topics |
|---|---|
| [Basics — Slices, Strings, Operators](Basics_Slice_String_Operators/) | Print, arithmetic, string indexing, slice notation, escape characters, f-strings, format specifiers |
| [Loops, Conditions, Ranges](Loops_Conditions_Ranges/) | `if`/`elif`/`else`, `for`, `while`, `range()`, `break`/`continue`, membership with `in`/`not in` |
| [Nesting, Tuples, and More Loops](Nesting_Tuples_MoreLoops/) | Lists vs tuples, mutability, nested data structures, `enumerate()`, `sorted()`, string methods |
| [Functions, Games, and Color Printing](Function_Games_ColorPrint/) | Function definitions, `*args`, iterative vs recursive implementations, ANSI color output, `colorama` |

### Intermediate
| Section | Topics |
|---|---|
| [Input / Output](Input_Output_Updated/) | File I/O, CSV (`reader`/`writer`/`DictReader`/`Sniffer`), JSON, `urllib.request`, `zip()` |
| [Object-Oriented Programming — Classes](ObjectOrientedProgramming_Classes/) | Class vs instance attributes, `__init__`, methods, `@staticmethod`, `property()`, `__dict__` |
| [Scope, Time & Tkinter](Scope_Time_Tkinter/) | Closures, `time`/`datetime`/`pytz`, Tkinter `pack`/`grid` layouts, Canvas, Blackjack game |
| [Shelves, Binary & Pickling](Shelves_Binary_Pickling/) | Text I/O, binary encoding, `pickle`, `shelve`, cave adventure game |
| [Supers, Subs, Sets, Copies & Hash](Supers_Subs_Sets_Copies_Hash/) | Dicts, `setdefault`/`get`, shallow vs deep copy, SHA-256 hashing, sets and all set operations |

### Advanced
| Section | Topics |
|---|---|
| [Errors and SQLite Continued](Errors_SqliteCont/) | `try`/`except`/`finally`, multiple exception types, SQLite CRUD, parameterized queries |
| [Classes Continued — Imports, SQLite, HTML](ClassCont_Imports_Sqlite_HTML/) | Duck typing, `property` decorator, SQLite with `Decimal` and timezone-aware timestamps, HTML generation |
| [Map, Filter, Reduce, Any, All](Map/) | `map()`, `filter()`, `functools.reduce()`, `any()`/`all()`, `namedtuple`, `timeit` benchmarking |
| [Generators, List Comprehensions, timeit](Genrators_ListComp_TimeIt/) | `yield`, lazy iteration, list/conditional/nested comprehensions, `timeit.repeat()`, `statistics` |
| [Big-O and Sorting](BigO_SortingFunctions/) | Bubble sort, O(n²) analysis, animated step-by-step terminal visualization with `colorama` |
| [Binary Files — Bytes, BMP, MP3](BinaryCont_Bytes_Bmp_Mp3/) | Byte manipulation, BMP pixel inversion, ID3v2 tag parsing, SHA-256 checksum verification |

### Applied Project
| Section | Topics |
|---|---|
| [MusicBrowser](MusicBrowser/) | Tkinter GUI music browser backed by SQLite — selecting an artist filters albums, selecting an album shows songs |

## Requirements

| Library | Install |
|---|---|
| `colorama` | `pip install colorama` |
| `pytz` | `pip install pytz` |
| `tkinter` | Included with standard Python |
| `sqlite3` | Included with standard Python |
| `hashlib` | Included with standard Python |
