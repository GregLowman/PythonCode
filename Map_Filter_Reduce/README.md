# Map, Filter, Reduce, Any, and All

Exercises covering Python's built-in higher-order functions — `map()`, `filter()`, `functools.reduce()`, `any()`, and `all()` — and how they compare to equivalent list comprehensions.

## Files

| File | Description |
|------|-------------|
| `Map_Intro.py` | `timeit` benchmark: list comprehension vs `map()` for capitalising characters and words |
| `filter_test.py` | List comprehension vs `filter()` for removing spam-containing meals; benchmarked with `timeit` |
| `reduce_intro.py` | `functools.reduce()` computing a product; compared with an explicit `for` loop |
| `any_all.py` | `any()` and `all()` with truthy/falsy values and empty-string truthiness |
| `allgotcha.py` | The `all()` gotcha: `all([])` returns `True` on an empty iterable; guard with `bool()` |
| `data.py` | Shared data module: people list and plant data as raw tuples, namedtuples, and a dict |
| `anycomprehensionm.py` | `any()` and `all()` applied to namedtuple plant data and a people email list |
| `named_plants.py` | Access namedtuple fields by name and use `_replace()` to produce a modified copy |

## Key Concepts

- **`map(func, iterable)`**: Applies a function to every element lazily; wrap in `list()` to materialise.
- **`filter(func, iterable)`**: Keeps elements for which `func` returns truthy.
- **`functools.reduce(func, iterable)`**: Folds a function across an iterable from left to right.
- **`any(iterable)`**: Returns `True` if at least one element is truthy (including generator expressions).
- **`all(iterable)`**: Returns `True` only if every element is truthy — but vacuously `True` on an empty iterable.
- **`collections.namedtuple`**: Lightweight, immutable record type with named field access; `_replace()` returns a modified copy.
