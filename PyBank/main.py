import os

import csv

print(dir(csv))

print(os.getcwd())


budgetcsv = os.path.join("Resources", "budget_data.csv")

# budgetcsv=r"\Resources\budget_data.csv"

with open(budgetcsv) as csv_file: 
    csv_reader = csv.reader(csv_file, delimiter = ",")

    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    for row in csv_reader:
        print(row)

    
