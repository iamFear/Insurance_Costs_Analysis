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

## Output

After executing `insurance.csv`, it'll generate a file in the same folder called `results.txt` that'll contain
the results of our analysis.
