import csv

with open('data/data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    data = {rows[1]:rows[0] for rows in reader}

print(data)
