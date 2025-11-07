import argparse
import sys

from tabulate import tabulate

from reader import read_products
from reports import REPORTS


def parse_args(argv=None):
    parser = argparse.ArgumentParser(
        description="Generate reports based on product CSV files."
    )
    parser.add_argument(
        "--files",
        nargs="+",
        required=True,
        help="Paths to CSV files with products data.",
    )
    parser.add_argument(
        "--report",
        required=True,
        help="Report name. For now supported: average-rating.",
    )
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)

    if args.report not in REPORTS:
        print(f"Unknown report: {args.report}", file=sys.stderr)
        print(f"Available reports: {', '.join(REPORTS.keys())}", file=sys.stderr)
        return 1

    try:
        rows = read_products(args.files)
    except FileNotFoundError as e:
        print(str(e), file=sys.stderr)
        return 1

    report_func = REPORTS[args.report]
    headers, table_rows = report_func(rows)

    print(tabulate(table_rows, headers=headers, showindex=range(1, len(table_rows) + 1), tablefmt="github"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())