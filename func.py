# coding=utf-8
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
from collections import Counter

class TimeKeeper:
    """Time Management for the exercice in seconds
    """
    # varialbles:
    # startTime
    # stopTime
    # totalDuration

    def __init__(self):
        pass
    
    def startTimer(self):
        self.startTime = datetime.datetime.today()

    def stopTimer(self):
        self.stopTime = datetime.datetime.today()

    def totalDuration(self):
        self.totalDuration = self.stopTime - self.startTime
        return self.totalDuration

    # # Initializer / Instance Attributes
    # def __init__(self, name):
    #     self.name = name
    #     # self.age = age

class Record(object):
    def __init__(self,recordFile, exercice):
        self.recordFile = recordFile
        self.setId(exercice)
        return

    def setId(self, exercice):
        currentDate = "{day}.{month}.{year}".format(year = exercice.timeKeeper.startTime.year, month=  exercice.timeKeeper.startTime.month, day=  exercice.timeKeeper.startTime.day)#datetime.date.today()
        currentTime = "{hour}:{minute}:{second}".format(hour = exercice.timeKeeper.startTime.hour, minute=  exercice.timeKeeper.startTime.minute, second=  exercice.timeKeeper.startTime.second)
        self.id = [currentDate, currentTime]
        choix =[]
        for key in exercice.choix:
            choix.append(exercice.choix[key])
        self.id = self.id + choix
        # exercice.choix['users'], exercice.choix['langue'], exercice.choix['voc'], exercice.choix['page'], exercice.choix['typeExercice'], exercice.choix['quoiEcrire'], exercice.choix['aide']]
        return

    def recordTentative(self, data):
        recordLine = []
        currentDateTime = datetime.datetime.today()
        currentDate = "{day}.{month}.{year}".format(year = currentDateTime.year, month=  currentDateTime.month, day=  currentDateTime.day)
        currentTime =  "{hour}:{minute}:{second}".format(hour = currentDateTime.hour, minute=  currentDateTime.minute, second=  currentDateTime.second)
        recordLine = self.id + [currentDate, currentTime] + data        
        myFile = open(self.recordFile, 'a', encoding="utf8")
        with myFile:
            recordsFile = csv.writer(myFile, delimiter=';', lineterminator='\n')
            recordsFile.writerows([recordLine])
        myFile.close()
        return

class ExerciceClass:
    """Exercice d'écriture
    """
    settings = {} # contient les differents settings globaux. E.g. sound ON/OFF, ...
    choix = {} # contient les différents choix de l utilisateur
    vocabulaire = {} # dict du vocabulaire de l'exercice en cours

    def __init__(self):
        self.timeKeeper = TimeKeeper()
        self.timeKeeper.startTimer()
        return
    
    def setVocabularies(self, vocabulary):
        self.vocabulaireBrut = vocabulary

        # Creation of sub vocabulary
        vocPhrase = {}
        vocMotSansDerDieDas = {}
        vocDerDieDasMot = {}
        vocMotTous = {}
        vocVerbe = {}
        for key in vocabulary:
            if vocabulary[key]['Type'] == "verbe":
                vocVerbe[key] = vocabulary[key]
            elif vocabulary[key]['Type'] == "phrase":
                vocPhrase[key] = vocabulary[key]
            elif vocabulary[key]['Type'] == "mot":
                vocMotTous[key] = vocabulary[key]
                if vocabulary[key]['Der-Die-Das'] =='' :
                    vocMotSansDerDieDas[key] = vocabulary[key]
                elif vocabulary[key]['Der-Die-Das'] !='' :
                    vocDerDieDasMot[key] = vocabulary[key]
                
        self.vocabulaire["vocabulaireBrut"]= vocabulary
        self.vocabulaire["vocPhrase"]={}
        self.vocabulaire["vocPhrase"]["elements"] = vocPhrase
        self.vocabulaire["vocMot"] = {}
        self.vocabulaire["vocMot"]["elements"] = vocMotSansDerDieDas
        self.vocabulaire["vocDerDieDasMot"] = {}
        self.vocabulaire["vocDerDieDasMot"]["elements"] = vocDerDieDasMot
        self.vocabulaire["vocMotTous"] = {}
        self.vocabulaire["vocMotTous"]["elements"] = vocMotTous
        self.vocabulaire["vocVerbe"] = {}
        self.vocabulaire["vocVerbe"]["elements"] = vocVerbe

        # (nbrDerDieDas,nbrMots,vocDerDieDasMot,nbrPhrases,nbrVerbes) = self.countElementsVocabulaire(vocabulary)
        self.vocabulaire["vocDerDieDasMot"]['nbrElements'] = self.countElementsVocabulaire(vocDerDieDasMot)
        self.vocabulaire["vocMot"]['nbrElements'] = self.countElementsVocabulaire(vocMotSansDerDieDas)
        self.vocabulaire["vocPhrase"]['nbrElements'] = self.countElementsVocabulaire(vocPhrase) 
        self.vocabulaire["vocVerbe"]['nbrElements'] = self.countElementsVocabulaire(vocVerbe) 
        return

    def countElementsVocabulaire(self, vocabulary):
        nbrElements = 0
        for key in vocabulary: 
            nbrElements += 1
        return (nbrElements)

    def addSettings(self, key, value):
        self.settings[key]=value
        return

    def addChoix(self, key, value):
        self.choix[key]=value
        return

    def ecrireQuoi(self):
        # if not (self.choix["quoiEcrire"] == "seulement der, die, das"): # cas standard, on emploie les voc tel quel.
        if self.choix["quoiEcrire"] == "phrase":
            voc = self.vocabulaire['vocPhrase']['elements']
        if self.choix["quoiEcrire"] == "verbe":
            voc = self.vocabulaire['vocVerbe']['elements']
        if self.choix["quoiEcrire"] == "mot":
            voc = self.vocabulaire['vocMotTous']['elements']
        if self.choix["quoiEcrire"] == "motDerDieDas": # On écrit le determinant + mot (das Schloss)
            voc = self.vocabulaire['vocDerDieDasMot']['elements']
            #Construction d un voc avec Der Die Das
            vocDerDieDas = {}
            for Key in voc:
                elementDDD = voc[Key]['Der-Die-Das'] + ' ' + voc[Key]['Mot en ALL']
                vocDerDieDas[Key] = voc[Key]
                vocDerDieDas[Key]['Mot en ALL'] = elementDDD
            voc = vocDerDieDas

        if self.choix["quoiEcrire"] == "seulement der, die, das": # On érite que le determinant (reponse: der / question: Schloss)
            voc =self.vocabulaire['vocDerDieDasMot']['elements']
            # nombreElements = len(voc)
            # countElements = 1
            vocNew = {}
            for key in voc:
                reponse = voc[key]['Der-Die-Das'] # reponse = "der"
                vocNew[key] = voc[key] # on commence avec le meme mot               
                vocNew[key]['Mot FR'] = voc[key]['Mot en ALL'] + ' (' + voc[key]['Mot FR'] +')' #indice "Freund (l'ami)"
                vocNew[key]['Mot en ALL'] = reponse 
            voc = vocNew
            
        motsDifficilesEtFrequence = self.ecrireVoc(voc) #on exerce le voc par écrit
        return motsDifficilesEtFrequence

        # else: # exception: trouver Der Die Das
        #     if self.choix["quoiEcrire"] == "seulement der, die, das":
        #         voc =self.vocabulaire['vocDerDieDasMot']['elements']
        #         # self.trouverDerDieDas(voc)
        #         nombreElements = len(voc) 
        #         countElements = 1
        #         keyMotsDifficiles = []
        #         for key in voc:
        #             elementAEcrire = voc[key]['Der-Die-Das'] # il faut écrire "der"
        #             indice = voc[key]['Mot en ALL'] # on donne "Freund"
        #             reponseAAfficher = elementAEcrire + ' ' + indice # la solution est "der Freund"
        #             reponseFausse = True
        #             tentative = 0
        #             while reponseFausse:
        #                 reponse = input('[{countElements}/{nombreElements}], [{nbrEssai} essai/{nbrEssaiTot}] Ecrire der, die ou das: [{mot}] '.format(mot= indice, nbrEssai = tentative+1,nbrEssaiTot=self.settings["nombreTentativeMax"], countElements=countElements, nombreElements=nombreElements ))
        #                 tentative += 1
        #                 if reponse == elementAEcrire:
        #                     print('Bravo')
        #                     reponseFausse = False
        #                     evaluationReponse = 'juste'
        #                     playSoundGoodOOP(self.settings)
        #                 else:
        #                     evaluationReponse = 'faux'
        #                     playSoundBadOOP(self.settings)
        #                     if self.choix["aide"] == "True": #choix.ecrireMotPhraseAide:
        #                         # showError(informationAEcrireEtranger, reponse)
        #                         showErrorString(elementAEcrire, reponse)
        #                 if tentative == self.settings['nombreTentativeMax']: # globalSettings.ecrireNombreTentativesMax: #si le nombre de tentative max est atteint on arrête.
        #                     keyMotsDifficiles.append(key)                    
        #                     break
        #             print('[{motFR}] est [{motEtranger}]\n'.format(motEtranger=reponseAAfficher, motFR = indice))
        #             countElements += 1
        # return motsDifficilesEtFrequence

    def lire(self):
        dictionnaire = {}
        # count = 0
        for keyVocabulaire in self.vocabulaire['vocabulaireBrut']:
            motATrouverFR = self.vocabulaire['vocabulaireBrut'][keyVocabulaire]['Mot FR']
            # newDic[keyVocabulaire] = motATrouverFR
            if self.vocabulaire['vocabulaireBrut'][keyVocabulaire]['Der-Die-Das'] != '':
                motATrouverEtrange = self.vocabulaire['vocabulaireBrut'][keyVocabulaire]['Der-Die-Das'] + " " + self.vocabulaire['vocabulaireBrut'][keyVocabulaire]['Mot en ALL']
            else:
                motATrouverEtrange = self.vocabulaire['vocabulaireBrut'][keyVocabulaire]['Mot en ALL']
            dictionnaire[keyVocabulaire] = {'question': motATrouverFR, 'reponse': motATrouverEtrange, 'indice': self.vocabulaire['vocabulaireBrut'][keyVocabulaire]['Type']}

        nbrElements = len(dictionnaire)  
        count = 0
        for motATrouverKey in dictionnaire: 
            print("{reste}/{total} [{TypeElement}]: {motATrouverFR} <<>> {motATrouverAll}".format(motATrouverFR= dictionnaire[motATrouverKey]['question'], motATrouverAll = dictionnaire[motATrouverKey]['reponse'], reste=count+1, total=nbrElements, TypeElement = dictionnaire[motATrouverKey]['indice']))
            pressEnter = input("")
            count = count + 1
        return
       
    def trouver(self):
             
        dictionnaire = {}
        # count = 0
        for keyVocabulaire in self.vocabulaire['vocabulaireBrut']:
            motATrouverFR = self.vocabulaire['vocabulaireBrut'][keyVocabulaire]['Mot FR']
            # newDic[keyVocabulaire] = motATrouverFR
            if self.vocabulaire['vocabulaireBrut'][keyVocabulaire]['Der-Die-Das'] != '':
                motATrouverEtrange = self.vocabulaire['vocabulaireBrut'][keyVocabulaire]['Der-Die-Das'] + " " + self.vocabulaire['vocabulaireBrut'][keyVocabulaire]['Mot en ALL']
            else:
                motATrouverEtrange = self.vocabulaire['vocabulaireBrut'][keyVocabulaire]['Mot en ALL']
            dictionnaire[keyVocabulaire] = {'question': motATrouverFR, 'reponse': motATrouverEtrange, 'indice': self.vocabulaire['vocabulaireBrut'][keyVocabulaire]['Type']}

        nbrElements = len(dictionnaire)  
        count = 0
        for motATrouverKey in dictionnaire: 
            
            #creation d'une liste sans le mot à trouver
            autresMots = dict(dictionnaire)
            del(autresMots[motATrouverKey])
            # on mélange les mots
            autresMotsKeys = list(autresMots.keys())
            random.shuffle(autresMotsKeys)
            # autresMotsKeys = {(key, autresMots[key]) for key in autresMotsKeys}
            # on choisi les x premiers mot à trouver
            countEnnemis =self.settings['nombreEnnemis']
            autresMotsEnnemisKeys = []
            for tmpKey in autresMotsKeys:
                if countEnnemis != 0:
                    autresMotsEnnemisKeys.append(tmpKey)
                    countEnnemis -= 1 
            #on construit la liste à montrer
            motsAMontrerKeys = []
            motsAMontrerKeys = autresMotsEnnemisKeys[:]
            # motsAMontrerKeys.append(keyVocabulaire)
            motsAMontrerKeys.append(motATrouverKey)


            # on mélange les mots
            random.shuffle(motsAMontrerKeys)
            # on construit la liste des mots a afficher
            # listeMotsEtrangeAMontrer = []
            # for key in motsAMontrerKeys:
            #     # if self.vocabulaire['vocabulaireBrut'][key]['Der-Die-Das'] != '':
            #     #     motAMontrer = str(self.vocabulaire['vocabulaireBrut'][key]['Der-Die-Das'] + " " + self.vocabulaire['vocabulaireBrut'][key]['Mot en ALL'])
            #     # else:
            #     #     motAMontrer = self.vocabulaire['vocabulaireBrut'][key]['Mot en ALL']
            #     listeMotsEtrangeAMontrer.append(motAMontrer)
            # On pose la question et on vérifie
            repeteQuestion = True
            pasReponduSouviens = True
            while repeteQuestion:
                print("{reste}/{total} [{TypeElement}]: Il faut trouver: '{motATrouverFR}'".format(motATrouverFR= dictionnaire[motATrouverKey]['question'], reste=count + 1, total=nbrElements, TypeElement = dictionnaire[motATrouverKey]['indice']))
                # valeurFausse = True                
                if pasReponduSouviens:
                    pasReponduSouviens = False
                    reponse = input('Te souviens tu du mot ? [ENTER] = oui, [1] = Non: ')                    
                    if reponse == '1':
                        jeMeSouviens = "Je me souviens pas"
                        # valeurFausse = False
                    else:
                        jeMeSouviens = "je me souviens"
                        # valeurFausse = False
                listeMotsEtrangeAMontrer = []
                for tmp in motsAMontrerKeys:    
                    listeMotsEtrangeAMontrer.append(dictionnaire[tmp]['reponse'])
                reponse = choisirElement(listeMotsEtrangeAMontrer)
                if reponse == dictionnaire[motATrouverKey]['reponse']:
                    repeteQuestion = False
                    evaluationReponse = "Juste"
                    print("{evaluation}: '{motFR}' = '{motEquivalent}'\n".format(
                        evaluation=evaluationReponse, motFR=dictionnaire[motATrouverKey]['question'], motEquivalent=dictionnaire[motATrouverKey]['reponse']))
                    # playSoundGood(globalSettings)
                    playSoundGoodOOP(self.settings)
                    # if globalSettings.soundActive == True:
                    #     winsound.PlaySound(
                    #         globalSettings.goodSound, winsound.SND_FILENAME)
                else:
                    repeteQuestion = True
                    evaluationReponse = "Faux"
                    print("{evaluation}: '{motFR}' n'est pas '{motEquivalent}'\n".format(
                        evaluation=evaluationReponse, motFR=motATrouverFR, motEquivalent=reponse))
                    # playSoundBad(globalSettings)
                    playSoundBadOOP(self.settings)
                resultatQuestion = [jeMeSouviens, evaluationReponse, dictionnaire[motATrouverKey]['reponse'], reponse]
                self.record.recordTentative(resultatQuestion)

            count = count + 1
        
        print("Enregistrement des exercices dans {fichier}".format(fichier = self.record.recordFile ))
        return

    def ecrireVoc(self, voc):
        indexTentative = 0
        keyMotsDifficiles = []
        nombreElementsTotal = len(voc)
        keysElements = [] # clef des éléments à exercer, évolue au cour de l exsercice, selon les fautes on étend la liste avec les mots difficile.
        for tmpKey in voc: # éléments de départ sont les éléments du voc.
            keysElements.append(tmpKey)
        ilResteDesElements = True
        while ilResteDesElements: #tant qu il reste des éléments on continue l exercice
            print('- Ecrire le mot sans le déterminant -\n{nombreElementsTotal} mots à apprendre\n{nbrElementsRestant} questions restantes\n'.format(indexTentative=indexTentative + 1, nombreElementsTotal=nombreElementsTotal, nbrElementsRestant = len(keysElements)-indexTentative ) )
            elementAEcrire = voc[keysElements[indexTentative]]['Mot en ALL']
            indice = voc[keysElements[indexTentative]]['Mot FR']
            if voc[keysElements[indexTentative]]['Der-Die-Das'] != '':
                reponseAAfficher = voc[keysElements[indexTentative]]['Der-Die-Das'] + ' ' + elementAEcrire
            else: 
                reponseAAfficher = elementAEcrire 

            reponseFausse = True
            tentative = 0
            pasRemisEnJeux = True
            # on refait la saisie tant que la réponse est fausse.
            while reponseFausse:
                reponse = input('[{nbrEssai} essai/{nbrEssaiTot}]: [{mot}] '.format(mot= indice, nbrEssai = tentative+1,nbrEssaiTot=self.settings["nombreTentativeMax"]))
                tentative += 1
                
                if reponse == elementAEcrire:
                    print('Bravo')
                    reponseFausse = False
                    evaluationReponse = 'juste'
                    playSoundGoodOOP(self.settings)
                else: # s'il y a une erreur dans la réponse
                    keyMotsDifficiles.append(keysElements[indexTentative]) # on ajout l éléments à la liste des éléments difficile
                    # keyMotsDifficiles[keysElements[indexElement]]=indexElement # on ajout l éléments à la liste des éléments difficile
                    if pasRemisEnJeux: # on remet l éléments dans la liste si ce n est pas déjà fait.
                        positionAjout = indexTentative + self.settings['deltaRemettreErreur']
                        keysElementsTmp = keysElements[:positionAjout]
                        keysElementsTmp.append(keysElements[indexTentative])
                        keysElementAfter =  keysElements[positionAjout:]
                        keysElements = keysElementsTmp + keysElementAfter
                        pasRemisEnJeux = False
                    evaluationReponse = 'faux'
                    playSoundBadOOP(self.settings)
                    if self.choix["aide"] == "True": #choix.ecrireMotPhraseAide:
                        # showError(informationAEcrireEtranger, reponse)
                        showErrorString(elementAEcrire, reponse)
                # on enregistre le résultat d'un élément exercé.                       
                resultatQuestion = [evaluationReponse, elementAEcrire, reponse]
                self.record.recordTentative(resultatQuestion) 
                # si on c'est trompé trop de foix, on passe à l'élément suivant
                if tentative == self.settings['nombreTentativeMax']:#si le nombre de tentative max est atteint on arrête.
                    break
            print('[{motFR}] est [{motEtranger}]\n'.format(motEtranger=reponseAAfficher, motFR = indice))
            print("")
            input('Appuyer sur ENTER')
            #Clear terminal screen 
            os.system('cls' if os.name == 'nt' else 'clear')
            
            #vérification s'il reste des éléments, si oui on continuera l'exercice
            if len(keysElements) == indexTentative + 1:
                ilResteDesElements = False
            indexTentative += 1
        # construction de la liste des mots diffiles

        motsDifficiles = {}
        # keyMotsDifficiles = ['1', '1', '3'] #for debug only 
        for tmpKey in keyMotsDifficiles:
            # mot = voc[tmpKey]
            motsDifficiles[tmpKey]=voc[tmpKey]
        #on calcul les stats
        frequenceErreur = Counter(keyMotsDifficiles)
        # frequenceErreur = Counter(MotsDifficiles)
        
        # on package dans un dict 
        motsDifficilesEtFrequence = {'motsDifficiles':motsDifficiles, 'frequenceErreur':frequenceErreur}
        return motsDifficilesEtFrequence


    def choixEcrireComment(self):
        print('Ecrire des mots ou des phrases ?')
        # optionChoisie = choisirElement([ 'tous les mots','mot avec der, die, das', 'seulement der, die, das', 'verbe','verbe avec aide', 'phrase', 'phrase avec aide'])
        optionChoisie = choisirElement([ 'tous les mots','mot avec der, die, das', 'seulement der, die, das', 'verbe', 'phrase'])

        if optionChoisie == 'mot':
            pass
        elif optionChoisie == 'tous les mots':
            self.addChoix("quoiEcrire","mot")
            self.addChoix("derDieDas","False")
            self.addChoix("aide","True")
        elif optionChoisie == 'mot avec der, die, das':
            self.addChoix("quoiEcrire","motDerDieDas")
            self.addChoix("derDieDas","True")
            self.addChoix("aide","True")
        elif optionChoisie == 'seulement der, die, das':
            self.addChoix("quoiEcrire","seulement der, die, das")
            self.addChoix("derDieDas","True")
            self.addChoix("aide","True")
        elif optionChoisie == 'phrase':
            self.addChoix("quoiEcrire","phrase")
            self.addChoix("aide","True")
        # elif optionChoisie == 'phrase avec aide':
        #     self.addChoix("quoiEcrire","phrase")
        #     self.addChoix("aide","True")
        elif optionChoisie == 'verbe':
            self.addChoix("quoiEcrire","verbe")
            self.addChoix("aide","True")
        # elif optionChoisie == 'verbe avec aide':
        #     self.addChoix("quoiEcrire","verbe")
        #     self.addChoix("aide","True")
        return

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
    # On compare 2 string et on montre ou se trouve la différence
    count = 0
    strDiff = ''
    lenJuste = len(strJuste)
    lenFaux = len(strFaux)
    if lenFaux > lenJuste:
        countMax = lenJuste
    else: countMax = lenFaux
    
    pasDeFaute = True
    while pasDeFaute:
        if count < countMax:
            if strJuste[count] == strFaux[count]:
                strDiff += strFaux[count]
            else:
                pasDeFaute = False
                strDiff += '^'
                strDiff += strFaux[count]
        else:
            pasDeFaute = False
            strDiff += '^'
        count += 1
    print('Il y a une erreur: ' + strDiff)
    return

def captureNumber(questionText):
    # Capture d'une string  qui ne peut etre qu'un chiffre
    isNotInteger = True
    while isNotInteger:

        userInput = input(questionText)
        #print("Is string: " + str(isinstance(userInput, str)))
        try:
            # val = int(userInput)
            int(userInput)
            isNotInteger = False
        except ValueError:
            print("Batar, ce n'est pas un chiffre !")
            isNotInteger = True
    return int(userInput)

# Selection d'un element parmis une liste d'élément
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
    # Recuperation du titre de l'exercice
    index = -1
    for exercicePossible in dataExercice.keys():
        index = index + 1
        if noExercice == index:
            nomExerciceChoisi = exercicePossible
    # Affichage du choix
    print("Tu as choisis: " + nomExerciceChoisi)
    return nomExerciceChoisi

def playSoundGood(globalSettings):
    # global globalSettings
    if globalSettings.soundActive == True:
        winsound.PlaySound(globalSettings.goodSound, winsound.SND_FILENAME)
    return

def playSoundBad(globalSettings):
    if globalSettings.soundActive == True:
        winsound.PlaySound(globalSettings.badSound, winsound.SND_FILENAME)
    return

def playSoundGoodOOP(settings):
    # global globalSettings
    if settings["activeSound"] == True:
        winsound.PlaySound(settings["good_sound"], winsound.SND_FILENAME)
    return

def playSoundBadOOP(settings):
    if settings["activeSound"] == True:
        winsound.PlaySound(settings["bad_sound"], winsound.SND_FILENAME)
    return

def trouverLeMot(vocabulaireList, choix, globalSettings):
    
    if choix.typeExerciceChoisi == "Trouver une correspondance":
        nombreMots = len(vocabulaireList)
        
        count = 0
        for keyVocabulaire in vocabulaireList:
            # motAtrouverKey = str(motAtrouverKey)
            motATrouverFR = vocabulaireList[keyVocabulaire]['Mot FR']
            
            if vocabulaireList[keyVocabulaire]['Der-Die-Das'] != '':
                motATrouverEtrange = vocabulaireList[keyVocabulaire]['Der-Die-Das'] + " " + vocabulaireList[keyVocabulaire]['Mot en ALL']
            else:
                motATrouverEtrange = vocabulaireList[keyVocabulaire]['Mot en ALL']
                    
            
            #creation d'une list sans le mot à trouver
            autresMots = dict(vocabulaireList)
            del(autresMots[keyVocabulaire])
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
            motsAMontrerKeys.append(keyVocabulaire)
            # on mélange les mots
            random.shuffle(motsAMontrerKeys)
            # on construit la liste des mots a afficher
            listeMotsEtrangeAMontrer = []
            for key in motsAMontrerKeys:
                if vocabulaireList[key]['Der-Die-Das'] != '':
                    motAMontrer = str(vocabulaireList[key]['Der-Die-Das'] + " " + vocabulaireList[key]['Mot en ALL'])
                else:
                    motAMontrer = vocabulaireList[key]['Mot en ALL']
                listeMotsEtrangeAMontrer.append(motAMontrer)
            # On pose la question et on vérifie
            repeteQuestion = True
            while repeteQuestion:
                print("{reste}/{total} [{TypeElement}]: Il faut trouver: '{motATrouverFR}'".format(
                    motATrouverFR=vocabulaireList[keyVocabulaire]['Mot FR'], reste=nombreMots - count, total=nombreMots, TypeElement = vocabulaireList[keyVocabulaire]['Type']))
                valeurFausse = True
                while valeurFausse:
                    reponse = input('Te souviens tu du mot ? [1] = oui, [ENTER] = Non: ')
                    if reponse == '1':
                        jeMeSouviens = True
                        valeurFausse = False
                    elif reponse == '':
                        jeMeSouviens = False
                        valeurFausse = False
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