# Messy People Data Analysis

A small data-cleaning and reporting pipeline that reads a "messy" CSV of people
records, cleans it (duplicates, missing values, word-to-number conversion),
computes summary statistics, and prints a report.

## How it works

The project is built in layers (`tool_kit_level_0` through `tool_kit_level_5`),
each building on the one before it. `main.py` only touches the top layers —
`DataSet`, `analyze`, and `Report` — everything else is used internally.

| File | Purpose |
|---|---|
| `tool_kit_level_0.py` | Standalone exploration script — loads the CSV with `csv.DictReader` and prints a preview. Not imported by the rest of the pipeline. |
| `tool_kit_level_1.py` | Defines the `Record` dataclass (`id`, `name`, `age`, `city`, `score`) with an `is_valid()` check for blank fields. |
| `tool_kit_level_2.py` | `DataCleaning` class: converts number-words ("twenty one" → `21`) and numeric strings to `int`/`float`, finds duplicate IDs with conflicting data (`findDuplicateID`), computes mean age/score and the most common name/city, and fills in missing values (`handle_missing_values`). |
| `tool_kit_level_3.py` | `DataSet` class: loads rows from the CSV, cleans each row (drops fully-blank rows and exact duplicate rows, converts to `Record`, fills missing values), and tracks counts (`rows_loaded`, `rows_cleaned`, `rows_dropped`, `dropped_reasons`, `duplicate_ids`). |
| `tool_kit_level_4.py` | `analyze(dataset)`: iterates the cleaned records to compute the average score, a per-city count dict, and the oldest/youngest `Record`. Timed via the `@log_call` decorator. |
| `tool_kit_level_5.py` | `Report` class: takes the dataset + computed stats and prints a formatted summary via `display()`. |
| `main.py` | Entry point — wires the above together and runs the report. |

## Requirements

- Python 3.10+ (uses `X | Y` union type hints)
- No third-party dependencies — only the standard library (`csv`, `time`, `dataclasses`)
- A CSV file named `messy_people.csv` with columns: `id, name, age, city, score`

## Usage

Place `messy_people.csv` in the same directory as the scripts (or update the
`filepath` variable in `main.py`), then run:

```bash
python main.py
```

This will:
1. Load `messy_people.csv` into a `DataSet`.
2. Clean each row — dropping blank/duplicate rows, converting number-words and
   numeric strings, and filling missing `age`/`score`/`name`/`city` values
   with computed averages/modes.
3. Analyze the cleaned records to get the average score, people-per-city
   counts, and the oldest/youngest person.
4. Print a report to the console, including load/clean/drop counts, flagged
   duplicate IDs (same ID, different data — kept for manual review), the
   average score, per-city breakdown, and oldest/youngest person.

## CSV format

Expected columns (header row required):

```
id,name,age,city,score
```

- `age` and `id` are parsed as integers; `score` as a float.
- Age/score fields may contain number-words (e.g. "twenty five") which are
  converted automatically.
- Blank `age`, `city`, or `score` values are filled in with the dataset's
  mean (for numeric fields) or mode (for `name`/`city`).
- Rows that are entirely blank (`age`, `city`, and `score` all empty) are
  dropped.
- Rows with an identical `id` but differing other fields are flagged in
  `duplicate_ids` for manual review rather than silently merged.

## Known issues / notes

- `tool_kit_level_3.DataSet.clean_row` recomputes dataset-wide statistics
  (`self.obj_data_clean.statistics(...)`) on every single row, which is
  redundant and could be slow on larger files — this could be hoisted out
  to run once per `DataSet` instead of once per row.
- `tool_kit_level_0.py` is a standalone exploratory script with a hardcoded
  absolute path; it isn't part of the `main.py` pipeline.

## Project Structure

```
.
├── main.py
├── tool_kit_level_0.py   # exploratory CSV preview script (standalone)
├── tool_kit_level_1.py   # Record dataclass
├── tool_kit_level_2.py   # DataCleaning, mean(), findDuplicateID()
├── tool_kit_level_3.py   # DataSet
├── tool_kit_level_4.py   # analyze()
├── tool_kit_level_5.py   # Report
└── messy_people.csv      # input data (not included)
```
