import csv
from pathlib import Path


def read_products(files):

    rows = []

    for file_path in files:
        path = Path(file_path)
        if not path.is_file():

            raise FileNotFoundError(f"File not found: {file_path}")

        with path.open(encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                rows.append(row)

    return rows