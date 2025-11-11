import csv

class CsvCombine:
    def __init__(self, files, output, encoding, final_headers):
        self.files_to_combine = files
        self.combined_data = []
        self.final_headers = final_headers
        self.file_header_map = dict()
        self.file_headers = set()
        self.common_headers = set()
        self.differing_headers = set()
        self.output_dir = output
        self.encoding = encoding

    def read_files(self):
        for file in self.files_to_combine:
            with open(file, "r", encoding=self.encoding) as f:
                csv_reader = csv.DictReader(f)
                header_row = csv_reader.fieldnames
                self.file_headers = self.file_headers.union(header_row)
                self.file_header_map[file] = set(header_row)
                rows = list(csv_reader)
                self.combined_data.extend(rows)
        print("Headers identified:", ", ".join(self.file_headers))
        print(len(self.combined_data), "records in total.")

    def get_header_info(self):
        common_headers = self.file_headers
        differing_headers = set()
        for file, headers in self.file_header_map.items():
            print(file, headers)
            common_headers = common_headers.intersection(headers)
        self.common_headers = common_headers
        print("Common Headers:", common_headers)
        differing_headers = self.file_headers.difference(common_headers)
        print("Differing Headers:", differing_headers)
        self.differing_headers = differing_headers
    
    def print_differing_header_source(self):
        for file, headers in self.file_header_map.items():
            differing_headers = headers.intersection(self.differing_headers)
            if differing_headers:
                print(f"Differing headers in file {file}:", differing_headers)

    def write_combined_data(self):
        with open(self.output_dir, "w", newline="", encoding=self.encoding) as f:
            writer = csv.DictWriter(f, fieldnames=list(self.final_headers), extrasaction="ignore")
            writer.writeheader()
            writer.writerows(self.combined_data)
    
    def set_final_headers(self):
        if not self.final_headers:
            self.final_headers = set(self.file_headers)

    def combine(self):
        self.read_files()
        self.get_header_info()
        self.print_differing_header_source()
        self.set_final_headers()
        self.write_combined_data()