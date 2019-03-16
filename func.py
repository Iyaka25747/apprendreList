import time
import winsound # Son, bruitage 
import os #for terminal screen clearing
from random import shuffle
import csv #for statistics logs
import random
import difflib # https://pymotw.com/2/difflib/ 
# from difflib_data import *
from pprint import pprint


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

def trouverLeMot(vocabulaireList, choix, globalSettings):
    
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
                resultatQuestion = [globalSettings.currentDate, globalSettings.currentTime, choix.nomJoueur, choix.nomLangueChoisie, choix.nomVocChoisi, choix.nomPageChoisie, choix.typeExerciceChoisi, evaluationReponse, motATrouverEtrange, reponse]
                # file = globalSettings.recordFile
                myFile = open( globalSettings.recordFile, 'a', encoding="utf8")
                with myFile:
                    recordsFile = csv.writer(myFile, delimiter=';', lineterminator='\n')
                    recordsFile.writerows([resultatQuestion])
                myFile.close()
            count = count + 1
        
    print("Enregistrement des exercices dans {fichier}".format(fichier = globalsetting.recordFile ))
    return

def ecrire(vocabulaireList, choix, globalSettings):
    countElements = 0
    # Identifier le nombre de mots ou de phrases  
    if choix.ecrireMotPhrase == "phrase":
        nombreElements = globalSettings.nbrMots
    else:
        nombreElements = globalSettings.nbrPhrase

    for key in vocabulaireList:
        # tentative += 1
        informationAEcrireEtranger = vocabulaireList[key]['Mot en ALL']
        informationAEcrireEtrangerComplet = vocabulaireList[key]['Der-Die-Das'] + ' '+ vocabulaireList[key]['Mot en ALL']
        informationAEcrireFR = vocabulaireList[key]['Mot FR']
        reponseFausse = True
        tentative = 0
        if vocabulaireList[key]['Type'] == choix.ecrireMotPhrase: #on fait que les mots ou les phrases
            while reponseFausse:
                reponse = input('[{countElementMP}/{nombreElements}], [{nbrEssai} essai/{nbrEssaiTot}] Ecrire le mot sans le déterminant: [{mot}] '.format(mot= informationAEcrireFR, nbrEssai = tentative+1,nbrEssaiTot=globalSettings.motNombreTentatives, countElements=countElements, nombreElements=nombreElements ))
                tentative += 1
                if reponse == informationAEcrireEtranger:
                    print('Bravo')
                    reponseFausse = False
                    evaluationReponse = 'juste'
                else:
                    evaluationReponse = 'faux'
                    if choix.ecrireMotPhraseAide:
                        showError(informationAEcrireEtranger, reponse)
                # record the results in a file
                tentativeProgress = '{countElementMP}/{nombreElements}; {nbrEssai} tentative/{nbrEssaiTot}'.format(nbrEssaiTot=globalSettings.motNombreTentatives, nbrEssai = tentative, countElements=countElements, nombreElements=nombreElements )

                resultatQuestion = [globalSettings.currentDate, globalSettings.currentTime, choix.nomJoueur, choix.nomLangueChoisie, choix.nomVocChoisi, choix.nomPageChoisie, choix.typeExerciceChoisi, tentativeProgress, evaluationReponse, informationAEcrireEtranger, reponse]
                myFile = open(globalSettings.recordFile, 'a', encoding="utf8")
                with myFile:
                    recordsFile = csv.writer(myFile, delimiter=';', lineterminator='\n')
                    recordsFile.writerows([resultatQuestion])
                myFile.close()
                if tentative == globalSettings.motNombreTentatives:
                    break
            print('[{motFR}] est [{motEtranger}]\n'.format(motEtranger=informationAEcrireEtrangerComplet, motFR = informationAEcrireFR))
    return

def ecrireLesMots(dataExercices, choix, globalSettings):
    vocabulaireList = dataExercices[choix.nomLangueChoisie][choix.nomVocChoisi][choix.nomPageChoisie]
    sorted(vocabulaireList)
    print('Ecrire des mots ou des phrases ?')
    # choixEcrireMots = ['mot', 'mot avec aide', 'phrase', 'phrase avec aide']
    e = choisirElement(['mot', 'mot avec aide', 'phrase', 'phrase avec aide'])
    # choix.ecrireMotPhrase = choisirElement(choixMP)
    if e == 'mot':
        choix.ecrireMotPhrase = 'mot'
        choix.ecrireMotPhraseAide = False
    elif e == 'mot avec aide':
        choix.ecrireMotPhrase = 'mot'
        choix.ecrireMotPhraseAide = True
    elif e == 'phrase':
        choix.ecrireMotPhrase = 'phrase'
        choix.ecrireMotPhraseAide = False
    elif e == 'phrase avec aide':
        choix.ecrireMotPhrase = 'phrase'
        choix.ecrireMotPhraseAide = True
    # nbrMots = 0
    # nbrPhrase = 0
    # # On compte les mots et les phrase dans la page
    # for key in vocabulaireList:
    #     if vocabulaireList[key]['Type'] == 'mot':
    #         nbrMots +=1
    #     elif vocabulaireList[key]['Type'] == 'phrase':
    #         nbrPhrase +=1
    
    # choix.typePhraseOuMot = "mot"
    # choix.motNombreTentatives = 3
    ecrire(vocabulaireList, choix, globalSettings)
    # countMots = 0
    # countPhrase = 0
    # for key in vocabulaireList:
    #     if vocabulaireList[key]['Type'] == choix.ecrireMotPhrase: #"mot": #on filtre les phrases
            
            # nombreElements = nbrMots
            # countMots += 1
            # motAecrireEtranger = vocabulaireList[key]['Mot en ALL']
            # motAecrireEtrangerComplet = vocabulaireList[key]['Der-Die-Das'] + ' '+ vocabulaireList[key]['Mot en ALL']
            # motAEcrireFR = vocabulaireList[key]['Mot FR']
            # reponseFausse = True
            # count = 0
            # while reponseFausse:
            #     reponse = input('[{countMots}/{nombreElements}], [{nbrEssai} essai/{nbrEssaiTot}] Ecrire le mot sans le déterminant: [{mot}] '.format(mot= motAEcrireFR, nbrEssai = count+1,nbrEssaiTot=choix.motNombreTentatives, countMots=countMots, nombreElements=nombreElements ))
            #     count += 1
            #     if reponse == motAecrireEtranger:
            #         print('Bravo')
            #         reponseFausse = False
            #         evaluationReponse = 'juste'
            #     else:
            #         evaluationReponse = 'faux'
            #         if choix.ecrireMotPhraseAide:
            #             showError(motAecrireEtranger, reponse)

            #     # record the results in a file
            #     tentativeProgress = '{countMots}/{nombreElements}; {nbrEssai} tentative/{nbrEssaiTot}'.format(nbrEssaiTot=choix.motNombreTentatives, nbrEssai = count, countMots=countMots, nombreElements=nombreElements )

            #     resultatQuestion = [globalSettings.currentDate, globalSettings.currentTime, choix.nomJoueur, choix.nomLangueChoisie, choix.nomVocChoisi, choix.nomPageChoisie, choix.typeExerciceChoisi, tentativeProgress, evaluationReponse, motAecrireEtranger, reponse]
            #     myFile = open(recordFile, 'a', encoding="utf8")
            #     with myFile:
            #         recordsFile = csv.writer(myFile, delimiter=';', lineterminator='\n')
            #         recordsFile.writerows([resultatQuestion])
            #     myFile.close()
            #     if count == choix.motNombreTentatives:
            #         break
            # print('[{motAEcrireFR}] est [{mot}]\n'.format(mot=motAecrireEtrangerComplet, motAEcrireFR = motAEcrireFR))

        # elif vocabulaireList[key]['Type'] == choix.ecrireMotPhrase: #"phrase":
        #     nombreElements = nbrMots
        #     countMots += 1
        #     motAecrireEtranger = vocabulaireList[key]['Mot en ALL']
        #     motAecrireEtrangerComplet = vocabulaireList[key]['Der-Die-Das'] + ' '+ vocabulaireList[key]['Mot en ALL']
        #     motAEcrireFR = vocabulaireList[key]['Mot FR']
        #     reponseFausse = True
        #     count = 0
        #     while reponseFausse:
        #         reponse = input('[{countMots}/{nombreElements}], [{nbrEssai} essai/{nbrEssaiTot}] Ecrire le mot sans le déterminant: [{mot}] '.format(mot= motAEcrireFR, nbrEssai = count+1,nbrEssaiTot=choix.motNombreTentatives, countMots=countMots, nombreElements=nombreElements ))
        #         count += 1
        #         if reponse == motAecrireEtranger:
        #             print('Bravo')
        #             reponseFausse = False
        #             evaluationReponse = 'juste'
        #         else:
        #             evaluationReponse = 'faux'
        #             # showError(motAecrireEtranger, reponse)

        #         # record the results in a file
        #         tentativeProgress = '{countMots}/{nombreElements}; {nbrEssai} tentative/{nbrEssaiTot}'.format(nbrEssaiTot=choix.motNombreTentatives, nbrEssai = count, countMots=countMots, nombreElements=nombreElements )

        #         resultatQuestion = [globalSettings.currentDate, globalSettings.currentTime, choix.nomJoueur, choix.nomLangueChoisie, choix.nomVocChoisi, choix.nomPageChoisie, choix.typeExerciceChoisi, tentativeProgress, evaluationReponse, motAecrireEtranger, reponse]
        #         myFile = open(recordFile, 'a', encoding="utf8")
        #         with myFile:
        #             recordsFile = csv.writer(myFile, delimiter=';', lineterminator='\n')
        #             recordsFile.writerows([resultatQuestion])
        #         myFile.close()
        #         if count == choix.motNombreTentatives:
        #             break
        #     print('[{motAEcrireFR}] est [{mot}]\n'.format(mot=motAecrireEtrangerComplet, motAEcrireFR = motAEcrireFR))
        # else:
        #     #print('Ce type n est pas prévu')
        #     pass
    
    return
