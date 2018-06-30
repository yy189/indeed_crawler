import os
import csv

def read_existing_companies(filename):
    existing_companies = set('')

    if os.path.isfile(filename):
        with open(filename, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                existing_companies.add(row['Organization Name'])

    return existing_companies