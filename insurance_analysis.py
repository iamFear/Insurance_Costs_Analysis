import csv

with open('insurance.csv', 'r') as file:
    reader = csv.reader(file)
    # for row in reader:
#     print(row)

    # Check the type of the reader
    print(type(reader))