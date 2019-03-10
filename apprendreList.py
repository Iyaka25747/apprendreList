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
exercicesFile = 'exercices_voc4.json'
with open(exercicesFile, 'r', encoding='utf8') as file:
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
myFile = open(recordFile, 'a', encoding="utf8")
print("Enregistrement des calculs dans {fichier}".format(fichier = recordFile ))
with myFile:
    writer = csv.writer(myFile, delimiter=',', lineterminator='\n')
    vocabulaireList = dataExercices[nomLangueChoisie][nomVocChoisi][nomPageChoisie]
    if nomLangueChoisie == "allemand":
        ############################
        # Trouver une correspondance
        ############################
        if typeExerciceChoisi == "Trouver une correspondance":
                nombreMots = len(vocabulaireList)
                nombreEnnemis = 4
                count = 0
                for keyAtrouver in vocabulaireList:
                    # motAtrouverKey = str(motAtrouverKey)
                    motATrouverFR = vocabulaireList[keyAtrouver]['Mot FR']
                    motATrouverEtrange = vocabulaireList[keyAtrouver]['Der-Die-Das']+" "+vocabulaireList[keyAtrouver]['Mot en ALL']
                    #creation d'une list sans le mot à trouver
                    autresMots = dict(vocabulaireList)
                    del(autresMots[keyAtrouver])
                    # on mélange les mots
                    autresMotsKeys = list(autresMots.keys())
                    random.shuffle(autresMotsKeys)
                    # autresMotsKeys = {(key, autresMots[key]) for key in autresMotsKeys}
                    # on choisi les x premiers mot à trouver
                    countEnnemis = nombreEnnemis
                    autresMotsEnnemisKeys = [] 
                    for key in autresMotsKeys:
                        if countEnnemis != 0:
                            autresMotsEnnemisKeys.append(key)
                            countEnnemis -= 1
                    #on construit la liste à montrer
                    motsAMontrerKeys = []
                    motsAMontrerKeys = autresMotsEnnemisKeys[:]
                    motsAMontrerKeys.append(keyAtrouver)
                    # on mélange les mots
                    random.shuffle(motsAMontrerKeys)
                    # on construit la liste des mots a afficher
                    listeMotsEtrangeAMontrer = []
                    for key in motsAMontrerKeys:
                        listeMotsEtrangeAMontrer.append(vocabulaireList[key]['Der-Die-Das'] + " " + vocabulaireList[key]['Mot en ALL'] )
                    # On pose la question et on vérifie
                    repeteQuestion = True
                    while repeteQuestion:
                        print("{reste}/{total} Comment dire: '{motATrouverFR}'".format(motATrouverFR=vocabulaireList[keyAtrouver]['Mot FR'], reste = nombreMots - count, total =nombreMots ))
                        
                        reponse = choisirElement(listeMotsEtrangeAMontrer)
                        if reponse == motATrouverEtrange:
                            repeteQuestion = False
                            evaluationReponse = "Juste"                
                            print("{evaluation}: '{motFR}' = '{motEquivalent}'\n".format(evaluation = evaluationReponse,motFR = motATrouverFR, motEquivalent = motATrouverEtrange))                    
                            if globalSettings.soundActive == True:
                                winsound.PlaySound(globalSettings.goodSound, winsound.SND_FILENAME)
                        else:
                            repeteQuestion = True
                            evaluationReponse = "Faux"   
                            print("{evaluation}: '{motFR}' n'est pas '{motEquivalent}'\n".format(evaluation = evaluationReponse,motFR = motATrouverFR, motEquivalent = reponse))
                            if globalSettings.soundActive == True:
                                winsound.PlaySound(globalSettings.badSound, winsound.SND_FILENAME)
                        resultatQuestion = [globalSettings.currentDate, globalSettings.currentTime, nomJoueur,nomLangueChoisie,nomVocChoisi,nomPageChoisie,typeExerciceChoisi,evaluationReponse, motATrouverEtrange,reponse]
                        writer.writerows([resultatQuestion])
                    count = count + 1
    #Enregistrement des statistiques
    # myFile = open(recordFile, 'a')
    # print("Enregistrement des calculs dans {fichier}".format(fichier = recordFile ))
    # with myFile:
    #     writer = csv.writer(myFile, delimiter=',', lineterminator='\n')
    #     writer.writerows([resultatQuestion])
print("Fin de l'enregistrement")
myFile.close()

print("\nOuf.... c'est fini ...")

fin = input("Terminé")

