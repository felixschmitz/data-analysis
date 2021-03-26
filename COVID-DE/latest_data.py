import csv

with open('COVID-RKI.csv', 'r') as f:
    reader = csv.reader(f,delimiter = ";")
    data = list(reader)
    row_count = len(data)
    latest = data[row_count - 1][0]
#date = df.at["row_count", "Datum"]
#print(latest)
