# Input / Output

Exercises covering file I/O, CSV reading and writing, JSON, and URL-based data fetching.

## Files

| File | Description |
|------|-------------|
| `Reading_A_Poem.py` | Read and print each line of a text file, stripping trailing newlines |
| `stripping.py` | Demonstrate `str.strip()`, `removeprefix()`, and `removesuffix()` on file content |
| `save_flowers.py` | Write a list to a text file using `print()` with a `file=` argument |
| `simple_json.py` | Write a list of tuples to JSON and read it back with `json.dump` / `json.load` |
| `global_temps.py` | Fetch and display NOAA global temperature anomaly data via `urllib.request` and `json` |
| `medals.py` | Read the 2020 Olympic medals CSV and print rows using `csv.reader` |
| `read_cereals.py` | Read cereal grain nutritional data from CSV; interactive grain lookup |
| `write_cereals.py` | Write cereal grain data to a quoted CSV file using `csv.writer` |
| `read_csv_dict.py` | Read a CSV into ordered dictionaries with `csv.DictReader` |
| `country_dialect.py` | Auto-detect CSV dialect with `csv.Sniffer` and read a pipe-delimited country file |
| `reading_country.py` | Parse a pipe-delimited country file manually; interactive capital lookup |
| `countries_dict_solution.py` | Parse country data with `csv.DictReader` and a custom delimiter; interactive capital lookup |
| `generate_medals_data.py` | Generate `medals_dict.py` by reading a CSV and writing a Python data structure |
| `medals_dict.py` | Hardcoded 2020 Olympic medals table; writes a sorted CSV via `csv.DictWriter` |
| `zipping_lists.py` | Use `zip()` to combine header keys with row tuples and write to CSV |
| `invoicing.py` | Append sequential invoice records to a tab-separated file; rolls the number over at the new year |

## Key Concepts

- **File modes**: `'r'`, `'w'`, `'r+'`, `'rb'`, `'wb'` — reading, writing, and read/write modes.
- **Context managers**: `with open(...) as f` ensures files are closed even if an error occurs.
- **`csv` module**: `reader`, `writer`, `DictReader`, `DictWriter`, `Sniffer` for dialect detection.
- **`json` module**: `json.dump` / `json.load` for serialising Python objects to/from JSON files.
- **`urllib.request`**: Fetching remote JSON data without third-party libraries.
- **`str.strip()` / `removeprefix()` / `removesuffix()`**: String cleaning methods for parsed text.
- **`zip()`**: Pairing iterables element-by-element to produce dictionaries from parallel lists.

## Assets Required

The following data files must be present in this directory to run the examples:

- `Jabberwocky.txt`
- `country_info.txt`
- `OlympicMedals_2020.csv`
- `cereal_grains.csv`
- `invoices.csv`
