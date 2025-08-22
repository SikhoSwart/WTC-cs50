import sys
import csv
from tabulate import tabulate

length = len(sys.argv)

if length < 2:
    sys.exit("Too few command-line arguments")
elif length > 2:
    sys.exit("Too many command-line arguments")
else:
    #CSV file
    csv_file = sys.argv[1]

if csv_file.endswith(".csv") == False:
    sys.exit("Not a CSV file")

else:
    table = []
    try:
        with open(csv_file) as file:
            reader = csv.reader(file)
            for line in reader:
                table.append([line[0], line[1], line[2]])
    except FileNotFoundError:
        sys.exit("File does not exist")

headers = table[0]
print(tabulate(table[1:], headers, tablefmt="grid"))

