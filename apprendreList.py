# Voc Anglais under work 2

import json
import random
import time #for measuring elapsed time, date
from func import *
import os #for terminal screen clearing
import winsound # Son, bruitage 
import datetime #for date
import time
import csv #for statistics logs

###############
#Initialisation
################

# Enregistrement des choix du joueur
class choixDuJoueur(object):
    """Global class to hold the settings"""
choix = choixDuJoueur()

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
exercicesFile = 'exercices_vocAll.json'
with open(exercicesFile, 'r', encoding='utf8') as file:
    dataExercices = json.load(file)
    file.close()
globalSettings.motNombreTentatives = 3 #Fixe le nombre de tentative avant de donner la réponse

#initialisation du fichier de statistiques
globalSettings.recordFile = "records.csv"
exerciceRecord = [] # Enregistrement d'un calculs "Date", "Time", "Joueur", "Nom du test", "Calcul", "nbr. Tentatives", "Duree"
recordsCalculs = [] # enregistrement des calculs faux pour les statistiques

# Affichage et selection du joueur
print("Joueurs: ")
users = dataSettings["users"]
choix.nomJoueur = choisirElement(users)

# Affichage et selection de la categorie Anglais, Allemand...
listElement = list(dataExercices.keys())
choix.nomLangueChoisie = choisirElement(listElement)

# Affichage et selection du Voc
listElement = list(dataExercices[choix.nomLangueChoisie].keys())
choix.nomVocChoisi = choisirElement(listElement)

# Affichage et selection de la page
listElement = list(dataExercices[choix.nomLangueChoisie][choix.nomVocChoisi].keys())
choix.nomPageChoisie = choisirElement(listElement)

#Affichage et selection du type d exercice "trouver le mot" ou "Orthographe Ecrire le mot"
typePossible = ["Trouver une correspondance", "Ecrire"]
print("Quel type d'exercice")
choix.typeExerciceChoisi = choisirElement(typePossible)

###########################
# Execution de l'exercice #
###########################

#Clear terminal screen 
os.system('cls' if os.name == 'nt' else 'clear')

vocabulaireList = dataExercices[choix.nomLangueChoisie][choix.nomVocChoisi][choix.nomPageChoisie]
nbrMots = 0
nbrPhrase = 0
# On compte les mots et les phrase dans la page
for key in vocabulaireList: 
    if vocabulaireList[key]['Type'] == 'mot':
        globalSettings.nbrMots +=1
    elif vocabulaireList[key]['Type'] == 'phrase':
        globalSettings.nbrPhrase +=1

if choix.nomLangueChoisie == "allemand":
    ############################
    # Trouver une correspondance
    ############################
    if choix.typeExerciceChoisi == "Trouver une correspondance":
        trouverLeMot(vocabulaireList, choix, globalSettings)
    elif choix.typeExerciceChoisi == "Ecrire":
        ecrireLesMots(vocabulaireList, choix, globalSettings)

print("\nOuf.... c'est fini ...")
fin = input("Terminé, presser une touche")


