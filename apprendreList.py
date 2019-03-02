# Voc Anglais under work 2

import json
import random
import time #for measuring elapsed time, date
from func import *
import os #for terminal screen clearing
import winsound # Son, bruitage 
import datetime #for date
import time
import csv #for statiristics logs

###############
# Initialisation
################

# Récupération des paramètres généraux
class SettingGlobal(object):
    """Global class to hold the settings"""
globalSettings = SettingGlobal()

with open("settings.json", "r") as file:
    dataSettings = json.load(file)
    file.close()

# Initialization des sons
soudSetting = dataSettings["son"]
if soudSetting["active"] == "on":
    globalSettings.soundActive = True
elif soudSetting["active"] == "off":
    globalSettings.soundActive = False
else:
    print("ERROR in setting parameter for -son- key")
    enterKey = input("press a key to continue")
globalSettings.badSound = soudSetting["bad_sound"]
globalSettings.goodSound = soudSetting["good_sound"]


# initialisation du temps
maintenant = datetime.datetime.today()
globalSettings.currentDate = "{day}.{month}.{year}".format(year = maintenant.year, month=  maintenant.month, day=  maintenant.day)#datetime.date.today()
globalSettings.currentTime = "{hour}:{minute}:{second}".format(hour = maintenant.hour, minute=  maintenant.minute, second=  maintenant.second)
print("Date: {0}, Time:{1}".format(globalSettings.currentDate, globalSettings.currentTime))

#Fichier source exercices
exercicesFile = 'exercices.json'
with open(exercicesFile, 'r') as file:
    dataExercices = json.load(file)
    file.close()

#initialisation du fichier de statistiques
recordFile = "records.csv"
exerciceRecord = [] # Enregistrement d'un calculs "Date", "Time", "Joueur", "Nom du test", "Calcul", "nbr. Tentatives", "Duree"
recordsCalculs = [] # enregistrement des calculs faux pour les statistiques

# Affichage et selection du joueur
print("Joueurs: ")
users = dataSettings["users"]
nomJoueur = choisirElement(users)

# Affichage et selection de la categorie Anglais, Allemand...
listElement = list(dataExercices.keys())
nomLangueChoisie = choisirElement(listElement)

# Affichage et selection du Voc
listElement = list(dataExercices[nomLangueChoisie].keys())
nomVocChoisi = choisirElement(listElement)

# Affichage et selection de la page
listElement = list(dataExercices[nomLangueChoisie][nomVocChoisi].keys())
nomPageChoisie = choisirElement(listElement)

#Affichage et selection du type d exercice "trouver le mot" ou "Orthographe Ecrire le mot"
typePossible = ["Trouver une correspondance", "Ecrire le mot"]
print("Quel type d'exercice")
typeExerciceChoisi = choisirElement(typePossible)

###########################
# Execution de l'exercice #
###########################

#Clear terminal screen 
os.system('cls' if os.name == 'nt' else 'clear')
vocabulaireList = dataExercices[nomLangueChoisie][nomVocChoisi][nomPageChoisie]
if nomLangueChoisie == "allemand":
  if typeExerciceChoisi == "Trouver une correspondance":
        nombreMots = len(vocabulaireList)
        nombreEnnemis = 4
        count = 0
        for motAtrouver in vocabulaireList:
            # motAtrouverKey = str(motAtrouverKey)
            motATrouverFR = vocabulaireList[motAtrouver]['Mot FR']
            motATrouverEquivalent = vocabulaireList[motAtrouver]['Der-Die-Das']+" "+vocabulaireList[motAtrouver]['Mot en ALL']
            #creation d'une list sans le mot à trouver
            autresMots = dict(vocabulaireList)
            del(autresMots[motAtrouver])
            xxxxx random.shuffle(autreMotKeys) # https://stackoverflow.com/questions/19895028/randomly-shuffling-a-dictionary-in-python
            # on choisi les x premiers mot à trouver
            autreMotKeys = autreMotKeys[:nombreEnnemis]
            #on construit la liste à montrer
            aTrouverMotsKeys = autreMotKeys[:]
            aTrouverMotsKeys.append(motAtrouverKey)
            random.shuffle(aTrouverMotsKeys)
            # construction des mots ennemis
            listeMotsEtranger = {}
            countMotAtrouver = 0
            for key in aTrouverMotsKeys:
                key = 'mot'+str(countMotAtrouver)
                listeMotsEtranger[key]= vocabulaireList['Der-Die-Das']+" "+vocabulaireList['Mot en ALL']
            # On pose la question et on vérifie
            repeteQuestion = True
            while repeteQuestion:
                print("{reste}/{total} Comment dire: '{motATrouver}'".format(motATrouver=motATrouverFR, reste = nombreMots - count, total =nombreMots ))
                reponse = choisirElement(listeMotsEtranger)
                if reponse == motATrouverEquivalent:
                    repeteQuestion = False
                    evaluationReponse = "Juste"                
                    print("{evaluation}: '{motFR}' = '{motEquivalent}'\n".format(evaluation = evaluationReponse,motFR = motATrouverFR, motEquivalent = motATrouverEquivalent))                    
                else:
                    repeteQuestion = True
                    evaluationReponse = "Faux"   
                    print("{evaluation}: '{motFR}' n'est pas '{motEquivalent}'\n".format(evaluation = evaluationReponse,motFR = motATrouverFR, motEquivalent = motATrouverEquivalent))
                resultatQuestion = [globalSettings.currentDate, globalSettings.currentTime, nomJoueur,nomLangueChoisie,nomVocChoisi,nomPageChoisie,typeExerciceChoisi,evaluationReponse, motATrouverEquivalent,reponse]
            count = count + 1

#Enregistrement des statistiques
myFile = open(recordFile, 'a')
print("Enregistrement des calculs dans {fichier}".format(fichier = recordFile ))
with myFile:
    writer = csv.writer(myFile, delimiter=',', lineterminator='\n')
    writer.writerows([resultatQuestion])
print("Fin de l'enregistrement")
myFile.close()

print("\nOuf.... c'est fini ...")

fin = input("Terminé")
