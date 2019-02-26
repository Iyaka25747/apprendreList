ligne = {"type":"Vocabulaire","DeterminantFR":"Le", "DetDE":"Das","NomFR":"Pain","NomDE":"Brot"}
print(ligne.get("DetDE"))

import csv

datafile = open('Voc6_1.csv', 'rt')
myreader = csv.DictReader(datafile, delimiter = ';')
for row in myreader:
    print(row)