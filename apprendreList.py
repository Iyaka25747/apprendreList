# Voc Anglais Under dev.

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
with open("settings.json", "r") as file:
    dataSettings = json.load(file)
    file.close()

# Initialization des sons
soudSetting = dataSettings["son"]
if soudSetting["active"] == "on":
    soundActive = True
elif soudSetting["active"] == "off":
    soundActive = False
else:
    print("ERROR in setting parameter for -son- key")
    enterKey = input("press a key to continue")
badSound = soudSetting["bad_sound"]
goodSound = soudSetting["good_sound"]


# initialisation du temps
maintenant = datetime.datetime.today()
currentDate = "{day}.{month}.{year}".format(year = maintenant.year, month=  maintenant.month, day=  maintenant.day)#datetime.date.today()
currentTime = "{hour}:{minute}:{second}".format(hour = maintenant.hour, minute=  maintenant.minute, second=  maintenant.second)
print("Date: {0}, Time:{1}".format(currentDate, currentTime))

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

# Affichage et selection mots/page
listElement = list(dataExercices[nomLangueChoisie][nomVocChoisi][nomPageChoisie].keys())
MotPageChoisie = choisirElement(listElement)

#Affichage et selection du type d exercice "trouver le mot" ou "Orthographe Ecrire le mot"
typePossible = ["Choisir une correspondance", "Ecrire le mot"]
print("Quel type d'exercice")
typeExerciceChoisi = choisirElement(typePossible)

###########################
# Execution de l'exercice #
###########################

#Clear terminal screen
os.system('cls' if os.name == 'nt' else 'clear')
vocabulaireList = dataExercices[nomLangueChoisie][nomVocChoisi][nomPageChoisie][MotPageChoisie]
if nomLangueChoisie == "Anglais":
  if typeExerciceChoisi == "Choisir une correspondance":
      motsFrancais = list(vocabulaireList.keys())
      motsAnglais = list(vocabulaireList.values())
      for motFrancaisDeviner in vocabulaireList.keys():
          print(motFrancaisDeviner)

#Enregistrement des statistiques
myFile = open(recordFile, 'a')
print("Enregistrement des calculs dans {fichier}".format(fichier = recordFile ))
with myFile:
    writer = csv.writer(myFile, delimiter=',', lineterminator='\n')
    writer.writerows(resultatsCalculs)
print("Fin de l'enregistrement")
myFile.close()

print("\nOuf.... c'est fini ...")

fin = input("Terminé")
