# Generators, List Comprehensions, and timeit

Exercises covering Python generators, list comprehensions, conditional comprehensions, nested comprehensions, and performance benchmarking with `timeit`.

## Files

| File | Description |
|------|-------------|
| `examples.py` | Generator function basics — `yield`, `next()`, and iteration |
| `size.py` | Custom `my_range` generator mimicking `range()` |
| `fibgen.py` | Fibonacci sequence generator |
| `filegen.py` | Generator that reads lines from a file one at a time |
| `filesearch.py` | Generator-based file search returning lines matching a keyword |
| `center_text.py` | Generator that center-pads each line of a file |
| `gen_challenge.py` | Generator challenge: iterate and yield from a data source |
| `GenChallenge.py` | Extended generator challenge |
| `listfor.py` | Side-by-side: `for` loop vs list comprehension producing the same result |
| `listComp.py` | List comprehension basics and filtering with conditions |
| `Challenge2.py` | List comprehension challenge |
| `challenge1.py` | Comprehension challenges: filtering and transforming sequences |
| `condcomp.py` | Conditional list comprehensions |
| `condcomp2.py` | Conditional comprehension with multiple conditions |
| `condcompChallenge1.py` | FizzBuzz implemented as a single list comprehension |
| `compchallenge2.py` | Comprehension challenge: find locations reachable from a given point in an adventure-game map |
| `compchallenge_2b.py` | Extended version of the location reachability challenge |
| `nested1.py` | Nested list comprehensions producing flat and grouped burger/topping pairs |
| `nested_challenge.py` | Nested vs flat comprehension timing comparison |
| `timeitchallenge.py` | `timeit` benchmark: iterative vs recursive factorial — timing, mean, and standard deviation |

## Key Concepts

- **Generators**: Functions using `yield` to produce values lazily without building a full list in memory.
- **List comprehensions**: Concise inline syntax for building lists, equivalent to filtered `for` loops.
- **Conditional comprehensions**: Inline `if`/`else` within comprehensions for filtering or mapping.
- **Nested comprehensions**: Comprehensions inside comprehensions for multi-dimensional data.
- **`timeit`**: Standard library module for benchmarking small code snippets across many repetitions.
- **`statistics`**: `mean()` and `stdev()` used alongside `timeit.repeat()` for statistical timing analysis.
