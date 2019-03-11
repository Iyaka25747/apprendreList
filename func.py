import time
import winsound # Son, bruitage 
import os #for terminal screen clearing
from random import shuffle
import csv #for statistics logs
import random

class NumberMulDiv(object):
    """ Represent a multiplication"""
    
# Capture d'un choix qui ne peut qu'un chiffre
def captureNumber(questionText):
    isNotInteger = True
    while isNotInteger:

        userInput = input(questionText)
        #print("Is string: " + str(isinstance(userInput, str)))
        try:
            val = int(userInput)
            isNotInteger = False
        except ValueError:
            print("Batar, ce n'est pas un chiffre !")
            isNotInteger = True
    return int(userInput)

# Selection d'un element valeur parmis une liste de valeur d'une list
def choisirElement(listOfValues):
    # Affichage des valeurs possibles
    position = 0
    for element in listOfValues:
        position = position + 1
        print("[{position}] {value}".format(position=position, value=element))
    #Choix d'une valeur
    choixFaux = True
    while choixFaux:
        capturedNumber = captureNumber("Choix: ")-1
        # on s assure que c'est un choix possible
        if capturedNumber >= len(listOfValues):
            choixFaux = True
        else:
            choixFaux = False
    chosenValue = listOfValues[capturedNumber]
    #print("Vous avez choisi: " + str(chosenValue))
    return chosenValue


# Fonction pour choisir un exercice dans un dictionnaire dataExercice
def choisirExercice(dataExercice):
    # affichage des exercices possibles    
    index = -1
    print("Liste des exercices:")
    for exercicePossible in dataExercice.keys():
        index = index + 1
        print("[{indexExercice}] Exercices: {exerciceNom}".format(indexExercice = index, exerciceNom = exercicePossible ))
    # Saisie du choix de l'exercice
    reponseFausse = True
    while reponseFausse:
        noExercice = captureNumber("Choix: ")
        if noExercice <= index:
            reponseFausse = False
    # Récupèration du titre de l'exercice
    index = -1
    for exercicePossible in dataExercice.keys():
        index = index + 1
        if noExercice == index:
            nomExerciceChoisi = exercicePossible
    # Affichage du choix
    print("Tu as choisis: " + nomExerciceChoisi)
    return nomExerciceChoisi

def trouverLeMot(recordFile, dataExercices, choix, globalSettings):
    vocabulaireList = dataExercices[choix.nomLangueChoisie][choix.nomVocChoisi][choix.nomPageChoisie]
    if choix.typeExerciceChoisi == "Trouver une correspondance":
        nombreMots = len(vocabulaireList)
        nombreEnnemis = 4
        count = 0
        for keyAtrouver in vocabulaireList:
            # motAtrouverKey = str(motAtrouverKey)
            motATrouverFR = vocabulaireList[keyAtrouver]['Mot FR']
            motATrouverEtrange = vocabulaireList[keyAtrouver]['Der-Die-Das'] + \
                " "+vocabulaireList[keyAtrouver]['Mot en ALL']
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
                listeMotsEtrangeAMontrer.append(
                    vocabulaireList[key]['Der-Die-Das'] + " " + vocabulaireList[key]['Mot en ALL'])
            # On pose la question et on vérifie
            repeteQuestion = True
            while repeteQuestion:
                print("{reste}/{total} Comment dire: '{motATrouverFR}'".format(
                    motATrouverFR=vocabulaireList[keyAtrouver]['Mot FR'], reste=nombreMots - count, total=nombreMots))

                reponse = choisirElement(listeMotsEtrangeAMontrer)
                if reponse == motATrouverEtrange:
                    repeteQuestion = False
                    evaluationReponse = "Juste"
                    print("{evaluation}: '{motFR}' = '{motEquivalent}'\n".format(
                        evaluation=evaluationReponse, motFR=motATrouverFR, motEquivalent=motATrouverEtrange))
                    if globalSettings.soundActive == True:
                        winsound.PlaySound(
                            globalSettings.goodSound, winsound.SND_FILENAME)
                else:
                    repeteQuestion = True
                    evaluationReponse = "Faux"
                    print("{evaluation}: '{motFR}' n'est pas '{motEquivalent}'\n".format(
                        evaluation=evaluationReponse, motFR=motATrouverFR, motEquivalent=reponse))
                    if globalSettings.soundActive == True:
                        winsound.PlaySound(
                            globalSettings.badSound, winsound.SND_FILENAME)
                resultatQuestion = [globalSettings.currentDate, globalSettings.currentTime, choix.nomJoueur, choix.nomLangueChoisie,
                                    choix.nomVocChoisi, choix.nomPageChoisie, choix.typeExerciceChoisi, evaluationReponse, motATrouverEtrange, reponse]
                myFile = open(recordFile, 'a', encoding="utf8")
                with myFile:
                    recordsFile = csv.writer(myFile, delimiter=',', lineterminator='\n')
                    recordsFile.writerows([resultatQuestion])
                myFile.close()
        count = count + 1
    print("Enregistrement des exercices dans {fichier}".format(fichier = recordFile ))
    return


def ecrireLesMots(recordFile, dataExercices, choix, globalSettings):
    vocabulaireList = dataExercices[choix.nomLangueChoisie][choix.nomVocChoisi][choix.nomPageChoisie]
    nbrMots = 0
    nbrPhrase = 0
    for key in vocabulaireList:
        if vocabulaireList[key]['Type'] == "mot":
            nbrMots +=1
        elif vocabulaireList[key]['Type'] == "phrase":
            nbrPhrase +=1
    
    # nombreElements = len(vocabulaireList)
    
    choix.typePhraseOuMot = "mot"
    choix.motNombreTentatives = 3
    if choix.typePhraseOuMot == "mot":  #on exerce l'écriture des mots
        countMots = 0
        countPhrase = 0
        for key in vocabulaireList:
            if vocabulaireList[key]['Type'] == "mot":
                nombreElements = nbrMots
                countMots += 1
                motAecrireEtranger = vocabulaireList[key]['Mot en ALL']
                motAEcrireFR = vocabulaireList[key]['Mot FR']
                reponseFausse = True
                count = 0
                while reponseFausse:
                    reponse = input('[{countMots}/{nombreElements}], [{nbrEssai} essai/{nbrEssaiTot}] Ecrire le mot sans le déterminant: [{mot}] '.format(mot= motAEcrireFR, nbrEssai = count+1,nbrEssaiTot=choix.motNombreTentatives, countMots=countMots, nombreElements=nombreElements ))
                    count += 1
                    if reponse == motAecrireEtranger:
                        print('Bravo')
                        reponseFausse = False
                    if count == choix.motNombreTentatives:
                        break
                print('[{motAEcrireFR}] est [{mot}]\n'.format(mot=motAecrireEtranger, motAEcrireFR = motAEcrireFR))
            elif vocabulaireList[key]['Type'] == "phrase":
                countPhrase += 1
                pass
            else:
                print('Ce type n est pas prévu')
                pass
            
    return