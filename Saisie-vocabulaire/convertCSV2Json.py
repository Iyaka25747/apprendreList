import csv
import json
from operator import itemgetter 
# #For YAML
# import yaml
# import io

inData = []
csvFile = open(r'C:\Users\ini\Documents\Development_Source_code\apprendreList\Saisie-vocabulaire\VocCSV.csv', 'rt', encoding="utf8")
jsonFile = open('C:\\Users\\ini\\Documents\\Development_Source_code\\apprendreList\\Voc-exercices.json', 'w', encoding="utf8")


reader = csv.DictReader(csvFile, delimiter = ';')

# build dictionnary from file
# voc;page;line;Type;Der-Die-Das;Mot en ALL;pluriel;Mot FR
lessonsDict = dict()
for row in reader:
    # Check if this language already exists
    language = row['language']
    if  language not in lessonsDict:
        lessonsDict[language] = {}
    # Check if this voc already exists
    voc = row['voc']
    if  voc not in lessonsDict[language]:
        lessonsDict[language][voc] = {}

    page = str(row['page'])
    if page not in lessonsDict[language][voc]:
        lessonsDict[language][voc][page]={}
    
    line = row['line']
    # if line not in lessonsDict[language][voc][page]:
    #     lessonsDict[language][voc][page][line]=[]

    del row['language']
    del row['voc']
    del row['page']
    del row['line']
    lessonsDict[language][voc][page][line] = row

#Le fichier transformer est sauver dans un fichier pour archive
json.dump(lessonsDict, jsonFile, indent=2, ensure_ascii=False )
jsonFile.write('\n')

# # Write YAML file
# with io.open('data.yaml', 'w', encoding='utf8') as outfile:
#     yaml.dump(lessonsDict, outfile, default_flow_style=False, allow_unicode=True)
