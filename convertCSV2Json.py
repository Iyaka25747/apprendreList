import csv
import json
from operator import itemgetter 

inData = []
csvFile = open('Voc6_1.csv', 'rt')
jsonFile = open('outfile_test.json', 'w')
reader = csv.DictReader(csvFile, delimiter = ';')

# build dictionnary from file
# voc;page;line;Type;Der-Die-Das;Mot en ALL;pluriel;Mot FR
lessonsDict = dict()
count = 0
for row in reader:
    # Check if this voc already exists
    voc = row['voc']
    if  voc not in lessonsDict:
        lessonsDict[voc] = {}

    page = str(row['page'])
    if page not in lessonsDict[voc]:
        lessonsDict[voc][page]=[]
    lessonsDict[voc][page].append(row)

    count += 1




prevVoc =""
prevPage =""
for row in reader:
    print(row)
    # group by - https://stackoverflow.com/questions/773/how-do-i-use-pythons-itertools-groupby 
    # https://adiyatmubarak.wordpress.com/2015/10/05/group-list-of-dictionary-data-by-particular-key-in-python/
    # students = sorted(students, key=itemgetter('class'))

    
    if count == 0: #skip the 1st line
        break
    while voc == prevVoc:
        while page == prevPage:
        #     body = tout les lignes meme voc meme page
                print("xx")
#     voc, page, line, motType, derDieDas, motEtranger, motFR = itemgetter(0,1,2,3,4,5,6)(row)

    json.dump(row, jsonFile)
    jsonFile.write('\n')