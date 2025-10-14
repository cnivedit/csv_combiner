import sys
import csv

combined_data = []
final_headers = ["Serial", "Name", "Age"]

def main(files):
    for file in files:
        with open(file, 'r') as f:
            csv_reader = csv.DictReader(f)
            rows = list(csv_reader)
            combined_data.extend(rows)

    with open("combined.csv", "w", newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=list(final_headers))
        writer.writeheader()
        writer.writerows(combined_data)

if __name__ == '__main__':
    files = sys.argv[1:]
    main(files)