# MusicBrowser

A Tkinter-based GUI application that browses a SQLite music database — selecting an artist filters the album list, and selecting an album shows its songs.

## Files

| File | Description |
|------|-------------|
| `jukebox.py` | Main application: `Scrollbox` and `DataListBox` Tkinter widgets backed by SQLite queries |
| `star_args.py` | Demonstrate `*args` and `**kwargs` by printing words and characters in reverse |

## Requirements

- Python 3 with `tkinter` (included in the standard library on most platforms)
- A `music.db` SQLite database in the same directory with `artists`, `albums`, and `songs` tables

## Running

```
python jukebox.py
```

## Key Concepts

- **`tkinter.Listbox` / `Scrollbar`**: Pairing a listbox with a vertical scrollbar via `yscrollcommand`.
- **`<<ListboxSelect>>` event**: Binding a callback to update dependent lists when a selection changes.
- **`sqlite3`**: Parameterised queries (`?` placeholders) to safely look up related rows.
- **`*args` / `**kwargs`**: Collecting and forwarding arbitrary positional and keyword arguments.
