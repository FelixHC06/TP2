import json
import csv

data = [
    (2, 3),
    (3, 2),
    (1.0, -5.3)
]

with open('data.json', 'w', encoding='UTF8') as f:
    json.dump(data, f)

with open('data.csv', 'w', newline='', encoding='utf-8') as fichier_csv:
    ecrivain_csv = csv.writer(fichier_csv)

    for reel in data:
        ecrivain_csv.writerow(reel)
