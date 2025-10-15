# CSV Combiner

A simple Python utility for combining user specified columns of multiple CSV files into one, even if their column orders differ.  

---

## Features

- Combine multiple CSV files with consistent or shuffled headers  
- Specify output filename and encoding  
- Choose which headers to include in the final output  

---

## Usage

### Run from the Command Line

```bash
python combine_csv.py file1.csv file2.csv [options]
````

### Available Options

| Flag | Long Form    | Description                                          | Default           |
| ---- | ------------ | ---------------------------------------------------- | ----------------- |
| `-o` | `--output`   | Output CSV file name                                 | `combined.csv`    |
| `-e` | `--encoding` | Encoding to use for reading/writing                  | `utf-8`           |
| `-H` | `--headers`  | Comma-separated list of headers for the final output | `Serial,Name,Age` |

---

## Examples

### Combine Two CSV Files

```bash
python combine_csv.py data1.csv data2.csv
```

### Specify a Custom Output File

```bash
python combine_csv.py data1.csv data2.csv -o merged_output.csv
```

### Use a Different Encoding

```bash
python combine_csv.py data1.csv data2.csv -e utf-16
```

### Define Custom Headers To Include

```bash
python combine_csv.py data1.csv data2.csv -H "Name,Email,Age"
```

---

## Requirements

* Python 3
* Standard Library only (no external dependencies)

---

## Output

By default, the combined CSV file is saved as:

```
combined.csv
```

You can change this with the `-o` or `--output` flag.

---

## Example Output

### Input files:

**file1.csv**

```csv
Serial,Name,Age
1,Alice,22
2,Bob,23
```

**file2.csv**

```csv
Name,Age,Serial,Email
Charlie,21,3,charlie@abc.com
Diana,24,4,diana@aad.com
```

### Command:

```bash
python combine_csv.py file1.csv file2.csv -o result.csv
```

### Output (`result.csv`):

```csv
Serial,Name,Age
1,Alice,22
2,Bob,23
3,Charlie,21
4,Diana,24
```
---