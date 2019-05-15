#Voc under work

import json
import random
import time #for measuring elapsed time, date
from func import *
import os #for terminal screen clearing
import winsound # Son, bruitage 
import datetime #for date, time
# import time
import csv #for statistics logs

###############
#Initialisation
################

debug = False
# debug = True
# debugLangue = "DE"
debugLangue = "EN"

exercice1 = ExerciceClass() # Un exercice pour mémoriser une liste d'information

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

#1 OOP- Initialization des sons
soudSetting = dataSettings["son"]
if soudSetting["active"] == "on":
    exercice1.addSettings("activeSound", True)
elif soudSetting["active"] == "off":
    exercice1.addSettings("activeSound", False)
else:
    print("ERROR in setting parameter for -son- key")
    enterKey = input("press a key to continue")
# globalSettings.badSound = soudSetting["bad_sound"]
# globalSettings.goodSound = soudSetting["good_sound"]
exercice1.addSettings("bad_sound",soudSetting["bad_sound"])
exercice1.addSettings("good_sound",soudSetting["good_sound"])

#1 ---- Initialization des sons
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

#2 OOP temps global. Si on fait plusieurs exercices
globalTimeKeeper = TimeKeeper()
globalTimeKeeper.startTimer()

#2 --- temps global. Si on fait plusieurs exercices
maintenant = datetime.datetime.today()
globalSettings.currentDate = "{day}.{month}.{year}".format(year = maintenant.year, month=  maintenant.month, day=  maintenant.day)#datetime.date.today()
globalSettings.currentTime = "{hour}:{minute}:{second}".format(hour = maintenant.hour, minute=  maintenant.minute, second=  maintenant.second)
print("Date: {0}, Time:{1}".format(globalSettings.currentDate, globalSettings.currentTime))

#Fichier source exercices
exercicesFile = 'Voc-exercices.json'
if debug:
    exercicesFile = 'exercices_vocAll_debug.json'

with open(exercicesFile, 'r', encoding='utf8') as file:
    dataExercices = json.load(file)
    file.close()
#OOP-
# globalSettings.ecrireNombreTentativesMax = 3 #Fixe le nombre de tentative max avant de donner la réponse pour les exercices d écriture
# globalSettings.nombreEnnemis = 4 # defini le nombre de mots total dans lequel trouver une correspondance
exercice1.addSettings("nombreTentativeMax", 3)
exercice1.addSettings("nombreEnnemis", 4)
exercice1.addSettings("deltaRemettreErreur", 3)

#----
globalSettings.ecrireNombreTentativesMax = 3 #Fixe le nombre de tentative max avant de donner la réponse pour les exercices d écriture
globalSettings.nombreEnnemis = 4 # defini le nombre de mots total dans lequel trouver une correspondance

#fichier de statistiques
globalSettings.recordFile = "records.csv"


exerciceRecord = [] # Enregistrement d'un calculs "Date", "Time", "Joueur", "Nom du test", "Calcul", "nbr. Tentatives", "Duree"
recordsCalculs = [] # enregistrement des calculs faux pour les statistiques

################################
##### CHOIX DU JOUEUR ##########
################################
if debug == True:
    if debugLangue == "EN":
        choix.nomJoueur = 'Ilya'
        choix.nomLangueChoisie = 'anglais'
        choix.nomVocChoisi = 'unit6'
        choix.nomPageChoisie = 'p60'
        print( '{} {} {} {}'.format(choix.nomJoueur, choix.nomLangueChoisie, choix.nomVocChoisi,  choix.nomPageChoisie))

    elif debugLangue == "DE":
        choix.nomJoueur = 'Ilya'
        choix.nomLangueChoisie = 'allemand'
        choix.nomVocChoisi = 'voc7'
        choix.nomPageChoisie = 'p45'

    exercice1.addChoix("users", choix.nomJoueur)
    exercice1.addChoix("langue", choix.nomLangueChoisie)
    exercice1.addChoix("voc", choix.nomVocChoisi)
    exercice1.addChoix("page", choix.nomPageChoisie)
else:
    #OOP- Supprimer la partie non OOP. Eg. choix.nomLangueChoisie = monchoix
    # Affichage et selection du joueur
    print("Joueurs: ")
    users = dataSettings["users"]
    monchoix = choisirElement(users)
    choix.nomJoueur = monchoix
    #OOP-
    exercice1.addChoix("users", monchoix)

    # Affichage et selection de la langue Anglais, Allemand...
    listElement = list(dataExercices.keys())
    monchoix = choisirElement(listElement)
    choix.nomLangueChoisie = monchoix #OOP - To delelte
    exercice1.addChoix("langue", monchoix)
    # Affichage et selection du Voc
    listElement = list(dataExercices[choix.nomLangueChoisie].keys())
    monchoix = choisirElement(listElement)
    choix.nomVocChoisi = monchoix #OOP - To delelte
    exercice1.addChoix("voc", monchoix)
    # Affichage et selection de la page
    listElement = list(dataExercices[choix.nomLangueChoisie][choix.nomVocChoisi].keys())
    monchoix = choisirElement(listElement)
    choix.nomPageChoisie = monchoix #OOP - To delelte
    exercice1.addChoix("page", monchoix)

    if debug == "True":
        exercice1.addChoix("TempsSprint", 1)
    else:
        exercice1.addChoix("TempsSprint", 10) # temps d'un sprint en minutes
    #OOP-FIN

#Affichage et selection du type d exercice "trouver le mot" ou "Orthographe Ecrire le mot"
typePossible = ["Lire les mots", "Trouver une correspondance", "Ecrire"]
print("Quel type d'exercice")
choix.typeExerciceChoisi = choisirElement(typePossible) #OOP - To delelte
exercice1.addChoix("typeExercice", choix.typeExerciceChoisi)
# exercice1.choix.append(}
# exercice1.choix.typeExerciceChoisi = choix.typeExerciceChoisi

#################################
####Exectution de l'exercice ####
#################################

#Clear terminal screen 
os.system('cls' if os.name == 'nt' else 'clear')

# Initialization des differents vocabulaires sur la base du vocabualire brute
vocabulaire = dataExercices[choix.nomLangueChoisie][choix.nomVocChoisi][choix.nomPageChoisie]
exercice1.setVocabularies(vocabulaire)

# test = ["rec1","rec2"]
# record.recordTentative(exercice1, test)

if choix.typeExerciceChoisi == "Lire les mots":
    # initialisation du fichier de statistique
    record = Record(globalSettings.recordFile, exercice1)
    exercice1.record = record
    exercice1.lire()
if choix.typeExerciceChoisi == "Trouver une correspondance":
    # initialisation du fichier de statistique
    record = Record(globalSettings.recordFile, exercice1)
    exercice1.record = record
    exercice1.trouver()
    # trouverLeMot(vocabulaire, choix, globalSettings)
elif choix.typeExerciceChoisi == "Ecrire":
    exercice1.choixEcrireComment()

    #initialisation du fichier de statistiques avec les choix
    # globalSettings.recordFile = "records.csv"
    record = Record(globalSettings.recordFile, exercice1)
    exercice1.record = record

    #exectution de l'exercice
    exercice1.ecrireQuoi()

globalTimeKeeper.stopTimer()
duree = globalTimeKeeper.totalDuration()
print("\nOuf.... c'est fini ...")
print("Durée de l'exercice: {duree}".format(duree=duree))
fin = input('Terminé, Tilio dit appuyer sur la touche \'enter\'')