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
# debugLangue = "EN"

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
#----
globalSettings.ecrireNombreTentativesMax = 3 #Fixe le nombre de tentative max avant de donner la réponse pour les exercices d écriture
globalSettings.nombreEnnemis = 4 # defini le nombre de mots total dans lequel trouver une correspondance


#initialisation du fichier de statistiques
#A faire plus tard: passer les enregistrements en OOP
globalSettings.recordFile = "records.csv"
exerciceRecord = [] # Enregistrement d'un calculs "Date", "Time", "Joueur", "Nom du test", "Calcul", "nbr. Tentatives", "Duree"
recordsCalculs = [] # enregistrement des calculs faux pour les statistiques

if debug == "True":
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
    #OOP-FIN

# Vocabulaire list contient tous les éléments (mot, phrase...) qui seront exercés
# Vocabulaire list est un dictionnaire:
# {"1": {"Type": "verbe","Der-Die-Das": "","Mot en ALL": "arrive, arrived","pluriel":"","Mot FR":"arriver"},"2": {"Type": etc
vocabulaireList = dataExercices[choix.nomLangueChoisie][choix.nomVocChoisi][choix.nomPageChoisie]

exercice1.setVocabulary(vocabulaireList)
# exercice1.printHello()


#Affichage et selection du type d exercice "trouver le mot" ou "Orthographe Ecrire le mot"
typePossible = ["Trouver une correspondance", "Ecrire"]
print("Quel type d'exercice")
choix.typeExerciceChoisi = choisirElement(typePossible) #OOP - To delelte
exercice1.addChoix("typeExercice", choix.typeExerciceChoisi)
# exercice1.choix.append(}
# exercice1.choix.typeExerciceChoisi = choix.typeExerciceChoisi

###########################
# Execution de l'exercice #
###########################

#Clear terminal screen 
os.system('cls' if os.name == 'nt' else 'clear')

# Initialization du nombre d'éléments à exercer
#OOP- count
# Au l'execution de la méthode setVocabulary les éléments sont comptés ...il n'y a plus besoins de faire un exercice1.countElementsVocabulaire()
#---- count
globalSettings.nbrMots = 0
globalSettings.nbrPhrases = 0
globalSettings.nbrVerbes = 0
globalSettings.nbrDerDieDas = 0
# On compte les mots et les phrase dans la page
for key in vocabulaireList: 
    if vocabulaireList[key]['Type'] == 'mot':
        globalSettings.nbrMots +=1
        if vocabulaireList[key]['Der-Die-Das'] != '':
            globalSettings.nbrDerDieDas +=1
    elif vocabulaireList[key]['Type'] == 'phrase':
        globalSettings.nbrPhrases +=1
    elif vocabulaireList[key]['Type'] == 'verbe':
        globalSettings.nbrVerbes +=1
#OOP - count FIN


#########################
## On lance l exercice ##
#########################
#OOP- execution

if choix.typeExerciceChoisi == "Trouver une correspondance":
    # exercice1.trouver()
    trouverLeMot(vocabulaireList, choix, globalSettings)
elif choix.typeExerciceChoisi == "Ecrire":
    # ecritureChoixTypeExercice(vocabulaireList, choix, globalSettings)
    sorted(vocabulaireList)
    print('Ecrire des mots ou des phrases ?')
    optionChoisie = choisirElement([ 'tous les mots','mot avec der, die, das', 'seulement der, die, das', 'verbe','verbe avec aide', 'phrase', 'phrase avec aide'])
    if optionChoisie == 'mot':
        pass
        # #OOP-
        # exercice1.addChoix("quoiEcrire","mot")
        # exercice1.addChoix("derDieDas","False")
        # exercice1.addChoix("aide","False")
        # #----
        # choix.ecrireMotPhrase = 'mot'
        # choix.ecrireDerDieDas = False
        # choix.ecrireMotPhraseAide = False
    elif optionChoisie == 'tous les mots':
        #OOP-
        exercice1.addChoix("quoiEcrire","mot")
        exercice1.addChoix("derDieDas","False")
        exercice1.addChoix("aide","True")
        #----
        choix.ecrireMotPhrase = 'mot'
        choix.ecrireDerDieDas = False
        choix.ecrireMotPhraseAide = True
    elif optionChoisie == 'mot avec der, die, das':
        #OOP-
        exercice1.addChoix("quoiEcrire","motDerDieDas")
        exercice1.addChoix("derDieDas","True")
        exercice1.addChoix("aide","True")
        #----
        choix.ecrireMotPhrase = 'mot'
        choix.ecrireDerDieDas = True
        choix.ecrireMotPhraseAide = False
    elif optionChoisie == 'seulement der, die, das':
        #OOP-
        exercice1.addChoix("quoiEcrire","seulement der, die, das")
        exercice1.addChoix("derDieDas","True")
        exercice1.addChoix("aide","True")
    elif optionChoisie == 'phrase':
        #OOP-
        exercice1.addChoix("quoiEcrire","phrase")
        exercice1.addChoix("aide","False")
        #----
        choix.ecrireMotPhrase = 'phrase'
        choix.ecrireMotPhraseAide = False
    elif optionChoisie == 'phrase avec aide':
        #OOP-
        exercice1.addChoix("quoiEcrire","phrase")
        exercice1.addChoix("aide","True")
        #----
        choix.ecrireMotPhrase = 'phrase'
        choix.ecrireMotPhraseAide = True
    elif optionChoisie == 'verbe':
        #OOP-
        exercice1.addChoix("quoiEcrire","verbe")
        exercice1.addChoix("aide","False")
        #----
        choix.ecrireMotPhrase = 'verbe'
        choix.ecrireMotPhraseAide = True
    elif optionChoisie == 'verbe avec aide':
        #OOP-
        exercice1.addChoix("quoiEcrire","verbe")
        exercice1.addChoix("aide","True")
        #----
        choix.ecrireMotPhrase = 'verbe'
        choix.ecrireMotPhraseAide = False
#OOP- execution FIN

exercice1.ecrire()
# ecrire(vocabulaireList, choix, globalSettings)

globalTimeKeeper.stopTimer()
duree = globalTimeKeeper.totalDuration()
print("\nOuf.... c'est fini ...")
print("Durée de l'exercice: {duree}".format(duree=duree))
fin = input('Terminé, Tilio dit appuyer sur la touche \'enter\'')