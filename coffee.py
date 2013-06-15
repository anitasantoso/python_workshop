import csv
f = open("airports.dat")

for row in csv.reader(f):
    data = row.split(",")
    city = data[2]
    airport = data[1]
    print(row)


