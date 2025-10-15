import sys
import csv

class CsvCombine:
    def __init__(self, files):
        self.files_to_combine = files
        self.combined_data = []
        self.final_headers = ["Serial", "Name", "Age"]
        self.file_headers = set()
        self.output_dir = "combined.csv"
        self.encoding = "utf-8"

    def read_files(self):
        for file in self.files_to_combine:
            with open(file, "r") as f:
                csv_reader = csv.DictReader(f)
                header_row = csv_reader.fieldnames
                self.file_headers = self.file_headers.union(header_row)
                rows = list(csv_reader)
                self.combined_data.extend(rows)
        print("Headers identified:", ", ".join(self.file_headers))
        print(len(self.combined_data), "records in total.")

    def write_combined_data(self):
        with open(self.output_dir, "w", newline="", encoding=self.encoding) as f:
            writer = csv.DictWriter(f, fieldnames=list(self.final_headers), extrasaction="ignore")
            writer.writeheader()
            writer.writerows(self.combined_data)
    
    def combine(self):
        self.read_files()
        self.write_combined_data()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("No input files provided. Unable to continue.")
        sys.exit(1)
    files = sys.argv[1:]
    csv_combiner = CsvCombine(files)
    csv_combiner.combine()