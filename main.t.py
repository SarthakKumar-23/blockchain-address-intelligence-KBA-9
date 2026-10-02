import csv

with open("data/addresses.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        address = row["address"]
        print(address)
