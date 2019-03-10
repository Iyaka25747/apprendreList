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

def executeMulitplication(listMultiplications, random, globalSettings, nomJoueur, nomTypeCalculChoisi, nomExerciceChoisi, modeExerciceChoisi):
    # Récupération des facteurs de multiplication de l exercice
    #facteursCalculs = dataExercices[nomTypeCalculChoisi][nomExerciceChoisi]
    premierFacteurs = listMultiplications["premier facteurs"]
    deuxiemeFacteurs = listMultiplications["deuxieme facteurs"]
    nombreDeCalculs = len(premierFacteurs) * len(deuxiemeFacteurs)
    print("Nombre de calculs à faire: {0}".format(nombreDeCalculs))

    # Exercices
    nombreCalculRestant = nombreDeCalculs
    tempsTotalDepart = time.perf_counter()
    nombreReponsesFaussesTot = 0
    recordsCalculs = []
    indexCalcul = 0
    for facteur1 in premierFacteurs:
        for facteur2 in deuxiemeFacteurs:
            reponseFausse = True
            nbrTentatives = 0
            tempsDepartCalcul = time.perf_counter()
            #recordCalcul = {}
            while reponseFausse:
                reponse = captureNumber("[{countDown} calculs restant] Entrer le résultat de {facteur1}x{facteur2}: ".format(
                    countDown=nombreCalculRestant, facteur1=facteur1, facteur2=facteur2))
                nbrTentatives = nbrTentatives + 1
                # vérification de la réponse
                if reponse == facteur1 * facteur2:
                    reponseFausse = False
                    if globalSettings.soundActive == True:
                        winsound.PlaySound(globalSettings.goodSound, winsound.SND_FILENAME)
                else:
                    reponseFausse = True
                    if globalSettings.soundActive == True:
                        winsound.PlaySound(globalSettings.badSound, winsound.SND_FILENAME)
                    # print("Peux faire mieux ...")
            indexCalcul = indexCalcul + 1
            nombreCalculRestant = nombreCalculRestant - 1
            calcul = "{facteur1}x{facteur2}".format(
                facteur1=facteur1, facteur2=facteur2)
            tempsFinCalcul = time.perf_counter()
            dureeCalcul = round(tempsFinCalcul - tempsDepartCalcul, 1)
            print("Nombre de tentatives: " + str(nbrTentatives))

            # enregistrement du resultat
            recordLine = [globalSettings.currentDate, globalSettings.currentTime , nomJoueur, nomTypeCalculChoisi, nomExerciceChoisi,modeExerciceChoisi, calcul, nbrTentatives, dureeCalcul]
            if nbrTentatives > 1:
                #calculsRecords.append(recordCalcul) # ajout à la liste
                recordsCalculs.append(recordLine)
            nombreReponsesFaussesTot = nombreReponsesFaussesTot + (nbrTentatives-1)
        
    #Statistiques globales
    tempsTotalFin = time.perf_counter()
    dureeExercice = round(tempsTotalFin - tempsTotalDepart, 1)
    print("temps passé: {tempsExercice} secondes, Nombre de réponses fausses: {totalReponseFaux}".format(tempsExercice = dureeExercice,totalReponseFaux = nombreReponsesFaussesTot))
    return recordsCalculs

def executeDivision(listFacteurs,random, globalSettings, nomJoueur, nomTypeCalculChoisi, nomExerciceChoisi,modeExerciceChoisi):
    # Récupération des facteurs de multiplication de l exercice
    #facteursCalculs = dataExercices[nomTypeCalculChoisi][nomExerciceChoisi]
    premierFacteurs = listFacteurs["premier facteurs"]
    deuxiemeFacteurs = listFacteurs["deuxieme facteurs"]
    
    #shuffle(deuxiemeFacteurs)
    #shuffle(premierFacteurs)
    dividendes = []
    for i in premierFacteurs:
        dividende = i * i
        dividendes.append([i, i, dividende])
        for n in deuxiemeFacteurs:
            dividende = i * n
            dividendes.append([i, n, dividende])
    for n in deuxiemeFacteurs:
            dividende = n * n
            dividendes.append([n, n, dividende])
    if random == 'True':
        shuffle(dividendes)
    nombreDeCalculs = len(dividendes)
    print("Nombre de calculs à faire: {0}".format(nombreDeCalculs))

    # Exercices
    nombreCalculRestant = nombreDeCalculs
    tempsTotalDepart = time.perf_counter()
    nombreReponsesFaussesTot = 0
    recordsCalculs = []
    indexCalcul = 0
    for calculItem in dividendes:
            calculText = "{dividende}/{diviseur}".format(dividende=calculItem[2], diviseur=calculItem[0])
            reponseFausse = True
            nbrTentatives = 0
            tempsDepartCalcul = time.perf_counter()
            #recordCalcul = {}
            while reponseFausse:
                reponse = captureNumber("[{countDown} calculs restant] Entrer le résultat de la division {calculText}: ".format(
                    countDown=nombreCalculRestant, calculText=calculText))
                nbrTentatives = nbrTentatives + 1
                # vérification de la réponse
                if reponse == calculItem[1]:
                    reponseFausse = False
                    if globalSettings.soundActive == True:
                        winsound.PlaySound(
                            globalSettings.goodSound, winsound.SND_FILENAME)
                else:
                    reponseFausse = True
                    if globalSettings.soundActive == True:
                        winsound.PlaySound(globalSettings.badSound, winsound.SND_FILENAME)
                    # print("Peux faire mieux ...")
            indexCalcul = indexCalcul + 1
            nombreCalculRestant = nombreCalculRestant - 1
            tempsFinCalcul = time.perf_counter()
            dureeCalcul = round(tempsFinCalcul - tempsDepartCalcul, 1)
            print("Nombre de tentatives: " + str(nbrTentatives))

            # enregistrement du resultat
            recordLine = [globalSettings.currentDate, globalSettings.currentTime, nomJoueur, nomTypeCalculChoisi,
                        nomExerciceChoisi, modeExerciceChoisi, calculText, nbrTentatives, dureeCalcul]
            if nbrTentatives > 1:
                #calculsRecords.append(recordCalcul) # ajout à la liste
                recordsCalculs.append(recordLine)
            nombreReponsesFaussesTot = nombreReponsesFaussesTot + \
                (nbrTentatives-1)

    #Statistiques globales
    tempsTotalFin = time.perf_counter()
    dureeExercice = round(tempsTotalFin - tempsTotalDepart, 1)
    print("temps passé: {tempsExercice} secondes, Nombre de réponses fausses: {totalReponseFaux}".format(
    tempsExercice=dureeExercice, totalReponseFaux=nombreReponsesFaussesTot))
    return recordsCalculs

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
