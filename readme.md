# Insurance Cost Analysis and Prediction

This project is related to Data Analysis for Businesses and uses `insurance.csv` to explore relationships between recorded personal characteristics and insurance costs values that are stored in a CSV file.

## Dataset

The CSV contains 1,338 records, no missing values, and one exact duplicate row in the initial inspection.

| Column | Description |
| --- | --- |
| `age` | Recorded age; observed range: 18–64 |
| `sex` | Recorded sex category |
| `bmi` | Body mass index |
| `children` | Recorded number of children |
| `smoker` | Recorded smoking status (`yes` or `no`) |
| `region` | Recorded region category |
| `charges` | Numeric cost value to analyze and predict |

### NOTE: All these values are fictional

## Intended capabilities

- Validate the data and investigate duplicates and unusual values.
- Summarize distributions and explore relationships between variables.
- (Pending to add specific functionalities)

## Project files

- `insurance.csv`: input dataset; preserve the original file.
- `insurance_analysis.py`: source code that takes care of the analysis.
- `readme.md`: project description.

## Usage and current capabilities

Requires Python 3 and uses only the standard-library `csv` module. Run from the
project directory using your terminal, so the relative path to `insurance.csv` resolves correctly:

```sh
python3 insurance_analysis.py
```

The script loads the CSV into `file_rows`, a dictionary whose zero-based keys
identify records. Each record is a dictionary mapping header names to values.
Duplicate records are preserved. Missing headers, empty or duplicate column
names, and records with too few or too many fields raise a `ValueError`.

For analysis, only complete records will be loaded: every column must contain
a non-empty value.
