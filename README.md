# Report Generator Lite

Python CLI tool that generates simple Markdown reports from CSV or JSON data.

The tool reads structured records from a `.csv` or `.json` file, detects available fields, creates a summary section, and writes sample records into a clean `.md` report.

## Features

- Generate Markdown reports from CSV files
- Generate Markdown reports from JSON files
- Automatically detect fields from input records
- Show total record count
- Include sample records in the report
- Control sample size with `--preview-limit`
- Custom report title with `--title`
- Simple CLI interface
- No external dependencies

## Tech Stack

- Python
- argparse
- csv
- json
- Markdown

## Project Structure

report-generator-lite/
  src/
    main.py
    loader.py
    report_builder.py
    writer.py
    logger_config.py

  data/
    .gitkeep

  README.md
  requirements.txt
  .gitignore

## Usage

Generate a report from a JSON file:

python src/main.py data/products.json data/report.md --title "Product Data Report" --preview-limit 5

Generate a report from a CSV file:

python src/main.py data/products.csv data/report.md --title "Product CSV Report" --preview-limit 3

## Arguments

input_file  
Path to the source `.csv` or `.json` file.

output_file  
Path where the generated Markdown report should be saved.

--title  
Optional report title. Default can be used if no title is provided.

--preview-limit  
Number of sample records to include in the report.

## Example JSON Input

[
  {
    "product_title": "Black Shirt",
    "price": "29.99",
    "sku": "SKU001"
  },
  {
    "product_title": "White Shirt",
    "price": "24.99",
    "sku": "SKU002"
  }
]

## Example CSV Input

product_title,price,sku
Black Shirt,29.99,SKU001
White Shirt,24.99,SKU002
Blue Hoodie,49.99,SKU003

## Example Output

# Product Data Report

## Summary

Source file: data/products.json  
Total records: 2  
Fields: product_title, price, sku

## Sample records

### Record 1

- product_title: Black Shirt
- price: 29.99
- sku: SKU001

### Record 2

- product_title: White Shirt
- price: 24.99
- sku: SKU002

## Notes

This project expects JSON input to be a list of records, where each record is an object.

Example:

[
  {
    "name": "Example",
    "price": "10.00"
  }
]

CSV files are read with headers, and each row becomes one record in the generated report.

## What I Practiced

- Building Python CLI tools with argparse
- Reading CSV files with csv.DictReader
- Reading JSON files with json.load
- Validating input data structure
- Generating Markdown text from structured data
- Saving generated reports to files
- Creating a small portfolio-ready data automation tool