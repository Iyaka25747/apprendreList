import csv
import json
from operator import itemgetter 

inData = []
csvFile = open('Voc6_1.csv', 'rt')
jsonFile = open('outfile_test.json', 'w')
fieldnames = ("voc","page","line","type","der-die-das","motEtranger","motFR")
reader = csv.reader(csvFile,fieldnames, delimiter = ';')

count = 0
prevVoc =""
prevPage =""
for row in reader:
    print(row)
    
    if count == 0: #skip the 1st line
        break
    while voc == prevVoc:
        while page == prevPage:
            body = tout les lignes meme voc meme page
    voc, page, line, motType, derDieDas, motEtranger, motFR = itemgetter(0,1,2,3,4,5,6)(row)

    json.dump(row, jsonFile)
    jsonFile.write('\n')