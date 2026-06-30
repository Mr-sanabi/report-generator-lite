import csv
import json
import os

def load_records(input_file):
    if input_file.endswith(".csv"):
        try:
            with open(input_file, "r", encoding="utf-8-sig", newline="") as file:
                reader = csv.DictReader(file)
                rows = []

                for row in reader:
                    rows.append(row)

                return rows

        except FileNotFoundError:
            print(f"File not found: {input_file}")
            return []
    elif input_file.endswith(".json"):
        if not os.path.exists(input_file):
            return []
        
        try:
            with open(input_file, "r", encoding="utf-8") as file:
                data = json.load(file)

                if not isinstance(data, list):
                    print("JSON file must contain a list of records")
                    return []

                return data 
        except json.JSONDecodeError as e:
            print(f"Error loading json file: {e}")
            return []
    
    else:
        print("Unsupported file type")
        return []