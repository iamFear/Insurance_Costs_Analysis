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

The script loads the CSV into `file_rows`, a list of dictionaries mapping header
names to values. `age` and `children` are converted to integers; `bmi` and
`charges` are converted to floats. Other values remain strings, and duplicate
records are preserved.

Running the script prints the average BMI for smokers and non-smokers and the
percentage difference relative to non-smokers. This is a descriptive comparison,
not evidence that smoking causes a BMI difference.

`count_key_values(key, checker)` counts exact matches in the loaded records and
returns an error message for an unknown column. Match numeric columns using
numbers rather than strings, for example `count_key_values("age", 19)`.

No prediction model or results-file output is implemented yet. The BMI comparison
requires at least one smoker and one non-smoker; otherwise it raises a
`ZeroDivisionError`. Header and row-shape validation are not currently implemented.

For analysis, only complete records will be loaded: every column must contain
a non-empty value. This is a requirement, not yet fully enforced: invalid or empty
numeric values fail conversion, but empty text values are still accepted.
