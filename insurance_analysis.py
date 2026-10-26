"""Load insurance records into a dictionary indexed by zero-based row number."""

import csv


def load_rows(file_path):
    """Return {row_number: {column: value}} with CSV values kept as strings.

    Preserve duplicate records. Reject empty or duplicate column names and
    rows whose number of values does not match the header.
    """
    with open(file_path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        headers = reader.fieldnames
        if not headers or any(not header.strip() for header in headers):
            raise ValueError("The CSV must have non-empty column names.")
        if len(headers) != len(set(headers)):
            raise ValueError("The CSV must have unique column names.")

        rows = {}
        for row_number, row in enumerate(reader):
            if None in row or None in row.values():
                raise ValueError(f"CSV record {row_number + 1} does not match the header.")
            rows[row_number] = row
        return rows


# Run from the project directory so this relative path finds the dataset.
file_rows = load_rows("insurance.csv")
