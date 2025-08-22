import sys
import csv

length = len(sys.argv)

if length < 3:
    sys.exit("Too few command-line arguments")
elif length > 3:
    sys.exit("Too many command-line arguments")
else:
    #CSV file
    csv_before = sys.argv[1]
    csv_after = sys.argv[2]

if csv_before.endswith(".csv") == False:
    sys.exit("Not a CSV file")
if csv_after.endswith(".csv") == False:
    sys.exit("Not a CSV file")

else:
    #list to store student info
    students = []
    try:
        with open(csv_before) as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append(row)
    except FileNotFoundError:
        sys.exit("File does not exist")

#create new file
with open(csv_after, "w") as file:
    fields = ["first", "last", "house"]
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()
    for student in students:
        #split the name into first and last name
        last, first = student["name"].split(",")
        house = student["house"]
        writer.writerow({"first": first.strip(), "last": last, "house": house})
