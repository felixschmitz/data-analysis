import csv
import requests
import os
from latest_data import *

CSV_URL = 'https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Projekte_RKI/Nowcasting_Zahlen_csv.csv?__blob=publicationFile'

with requests.Session() as s:
    download = s.get(CSV_URL)
    decoded_content = download.content.decode('utf-8')
    cr = csv.reader(decoded_content.splitlines(), delimiter=';')

    my_list = list(cr)
    out = csv.writer(open('COVID-RKI.csv', 'w'), delimiter=';', quoting=csv.QUOTE_ALL)
    for row in my_list:
        if any(row):
            out.writerow(row)
            #print(row)
        else:
            break
os.system('python latest_data.py')
print('Data has been refreshed. The latest data is from: ' + latest)
