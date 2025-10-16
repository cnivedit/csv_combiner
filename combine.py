import argparse
from csvcombine.csv_combiner import CsvCombine

def csv_combiner():
    parser = argparse.ArgumentParser(
        description="Combine multiple CSV files with flexible options."
    )

    parser.add_argument(
        "files",
        nargs="+",
        help="List of input CSV files to combine."
    )

    parser.add_argument(
        "-o", "--output",
        default="combined.csv",
        help="Output CSV file name (default: combined.csv)"
    )

    parser.add_argument(
        "-e", "--encoding",
        default="utf-8",
        help="Encoding to use for reading and writing (default: utf-8)"
    )

    parser.add_argument(
        "-H", "--headers",
        default="Serial,Name,Age",
        help="Comma-separated list of final headers (default: Serial,Name,Age)"
    )

    args = parser.parse_args()

    final_headers = [h.strip() for h in args.headers.split(",")]

    csv_combiner = CsvCombine(
        files=args.files,
        output=args.output,
        encoding=args.encoding,
        final_headers=final_headers
    )
    csv_combiner.combine()


if __name__ == "__main__":
    csv_combiner()