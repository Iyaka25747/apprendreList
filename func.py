import time
import winsound # Son, bruitage 
import os #for terminal screen clearing
from random import shuffle
import csv #for statistics logs
import random
import difflib # https://pymotw.com/2/difflib/ 
# from difflib_data import *
from pprint import pprint
# import time #for measuring elapsed time, date
import datetime #for date, time


class NumberMulDiv(object):
    """ Represent a multiplication"""
    
def showError(texteJuste, texteFaux):
    texteJuste = [texteJuste]
    texteFaux = [texteFaux]
    d = difflib.Differ()
    # diff = d.compare(text2, text1)
    result = list(d.compare(texteFaux, texteJuste))
    # result = list(difflib.ndiff(texteFaux, texteJuste))
    for text in result:
        text = text.strip()
        print('     ' + text)
    return

def showErrorString(strJuste, strFaux):
    count = 0
    strDiff = ''
    pasDeFaute = True
    while pasDeFaute:
        if count < len(strFaux):
            if strJuste[count] == strFaux[count]:
                strDiff += strFaux[count]
            else:
                pasDeFaute = False
                strDiff += '^'
                strDiff += strFaux[count:]
        else:
            pasDeFaute = False
            strDiff += '^'
            strDiff += strFaux[count:]

        count += 1
    print('Il y a une erreur: ' + strDiff)
    return

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

def playSoundGood(globalSettings):
    if globalSettings.soundActive == True:
        winsound.PlaySound(globalSettings.goodSound, winsound.SND_FILENAME)
    return

def playSoundBad(globalSettings):
    if globalSettings.soundActive == True:
        winsound.PlaySound(globalSettings.badSound, winsound.SND_FILENAME)
    return

def trouverLeMot(vocabulaireList, choix, globalSettings):
    
    if choix.typeExerciceChoisi == "Trouver une correspondance":
        nombreMots = len(vocabulaireList)
        
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
            countEnnemis =globalSettings.nombreEnnemis
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
            
            #     listeMotsEtrangeAMontrer.append(vocabulaireList[key]['Der-Die-Das'] + " " + vocabulaireList[key]['Mot en ALL'])


            # for key in motsAMontrerKeys:
            #     if vocabulaireList[key]['Type'] == 'mot':
            #         motAMontrer = vocabulaireList[key]['Der-Die-Das'] + " " + vocabulaireList[key]['Mot en ALL']
            #     else:
            #         motAMontrer = vocabulaireList[key]['Mot en ALL']
            for key in motsAMontrerKeys:
                motAMontrer = str(vocabulaireList[key]['Der-Die-Das'] + " " + vocabulaireList[key]['Mot en ALL'])
                listeMotsEtrangeAMontrer.append(motAMontrer)
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
                    playSoundGood(globalSettings)
                    # if globalSettings.soundActive == True:
                    #     winsound.PlaySound(
                    #         globalSettings.goodSound, winsound.SND_FILENAME)
                else:
                    repeteQuestion = True
                    evaluationReponse = "Faux"
                    print("{evaluation}: '{motFR}' n'est pas '{motEquivalent}'\n".format(
                        evaluation=evaluationReponse, motFR=motATrouverFR, motEquivalent=reponse))
                    playSoundBad(globalSettings)
                resultatQuestion = [globalSettings.currentDate, globalSettings.currentTime, choix.nomJoueur, choix.nomLangueChoisie, choix.nomVocChoisi, choix.nomPageChoisie, choix.typeExerciceChoisi, evaluationReponse, motATrouverEtrange, reponse]
                
                recordTentative(resultatQuestion, globalSettings)                
            count = count + 1
        
    print("Enregistrement des exercices dans {fichier}".format(fichier = globalSettings.recordFile ))
    return

def recordTentative(resultatQuestion, globalSettings):
    myFile = open(globalSettings.recordFile, 'a', encoding="utf8")
    with myFile:
        recordsFile = csv.writer(myFile, delimiter=';', lineterminator='\n')
        recordsFile.writerows([resultatQuestion])
    myFile.close()
    return

def ecrire(vocabulaireList, choix, globalSettings):
    countElements = 0
    keyMotsDifficiles = []
    startTime = datetime.datetime.today()
    # os.system('cls' if os.name == 'nt' else 'clear') #Clear terminal screen
    # Identifier le nombre de mots ou de phrases  
    if choix.ecrireMotPhrase == "phrase":
        nombreElements = globalSettings.nbrPhrases
    elif choix.ecrireMotPhrase == "mot":
        nombreElements = globalSettings.nbrMots
    elif choix.ecrireMotPhrase == "verbe":
        nombreElements = globalSettings.nbrVerbes
    # else:
    #     nombreElements = globalSettings.nbrPhrase

    for key in vocabulaireList:

        informationAEcrireEtranger = vocabulaireList[key]['Mot en ALL']
        informationAEcrireEtrangerComplet = vocabulaireList[key]['Der-Die-Das'] + ' '+ vocabulaireList[key]['Mot en ALL']
        informationAEcrireFR = vocabulaireList[key]['Mot FR']
        reponseFausse = True
        tentative = 0
        if vocabulaireList[key]['Type'] == choix.ecrireMotPhrase: #on ne fait que les mots ou les phrases ...
            # os.system('cls' if os.name == 'nt' else 'clear') #Clear terminal screen 
            while reponseFausse:
                reponse = input('[{countElements}/{nombreElements}], [{nbrEssai} essai/{nbrEssaiTot}] Ecrire le mot sans le déterminant: [{mot}] '.format(mot= informationAEcrireFR, nbrEssai = tentative+1,nbrEssaiTot=globalSettings.ecrireNombreTentativesMax, countElements=countElements, nombreElements=nombreElements ))
                tentative += 1
                if reponse == informationAEcrireEtranger:
                    print('Bravo')
                    reponseFausse = False
                    evaluationReponse = 'juste'
                    playSoundGood(globalSettings)
                else:
                    evaluationReponse = 'faux'
                    playSoundBad(globalSettings)
                    if choix.ecrireMotPhraseAide:
                        # showError(informationAEcrireEtranger, reponse)
                        showErrorString(informationAEcrireEtranger, reponse)

                # create the entry for the record
                repsonseLog = '{countElements}/{nombreElements}; {nbrEssai} tentative/{nbrEssaiTot}'.format(nbrEssaiTot=globalSettings.ecrireNombreTentativesMax, nbrEssai = tentative, countElements=countElements, nombreElements=nombreElements )
                entryLog = [globalSettings.currentDate, globalSettings.currentTime, choix.nomJoueur, choix.nomLangueChoisie, choix.nomVocChoisi, choix.nomPageChoisie, choix.typeExerciceChoisi, repsonseLog, evaluationReponse, informationAEcrireEtranger, reponse]
                # Log the attempt in a file
                recordTentative(entryLog, globalSettings)

                if tentative == globalSettings.ecrireNombreTentativesMax: #si le nombre de tentative max est atteint on arrête.
                    keyMotsDifficiles.append(key)                    
                    break
            print('[{motFR}] est [{motEtranger}]\n'.format(motEtranger=informationAEcrireEtrangerComplet, motFR = informationAEcrireFR))
            countElements += 1
            # break
        # enregistre les mots difficiles
    # stopTime = datetime.datetime.today()
    # deltaTime = stopTime - startTime
    # test = stopTime.second
    # print(test)
    # print('Temps de l exercice: {minutes}min. et {seconde}sec.'.format(minutes=deltaTime.minute, seconde=deltaTime.second))
    # print('hello')
    return

def ecrireLesMots(vocabulaireList, choix, globalSettings):
    sorted(vocabulaireList)
    print('Ecrire des mots ou des phrases ?')
    optionChoisie = choisirElement(['mot', 'mot avec aide', 'phrase', 'phrase avec aide', 'verbe','verbe avec aide'])
    if optionChoisie == 'mot':
        choix.ecrireMotPhrase = 'mot'
        choix.ecrireMotPhraseAide = False
    elif optionChoisie == 'mot avec aide':
        choix.ecrireMotPhrase = 'mot'
        choix.ecrireMotPhraseAide = True
    elif optionChoisie == 'phrase':
        choix.ecrireMotPhrase = 'phrase'
        choix.ecrireMotPhraseAide = False
    elif optionChoisie == 'phrase avec aide':
        choix.ecrireMotPhrase = 'phrase'
        choix.ecrireMotPhraseAide = True
    elif optionChoisie == 'verbe':
        choix.ecrireMotPhrase = 'verbe'
        choix.ecrireMotPhraseAide = True
    elif optionChoisie == 'verbe avec aide':
        choix.ecrireMotPhrase = 'verbe'
        choix.ecrireMotPhraseAide = False
    ecrire(vocabulaireList, choix, globalSettings)
    return
