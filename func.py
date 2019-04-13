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

class ExerciceClass:
    """Exercice d'écriture
    """
    settings = {} # contient les differents settings globaux. E.g. sound ON/OFF, ...
    choix = {} # contient les différents choix de l utilisateur
    # vocabulaireBrut = {} # contient une page de vocabulaire
    # vocMot ={} # que les mots
    # vocPhrase = {} # que les phrase
    # vocVerbe = {} # que les verbes
    vocabulaire = {}

    def __init__(self):
        self.timeKeeper = TimeKeeper()
        self.timeKeeper.startTimer()
        return
    
    def setVocabulary(self, vocabulary):
        self.vocabulaireBrut = vocabulary

        # Creation of sub vocabulary
        vocPhrase = {}
        vocMot = {}
        vocDerDieDasMot = {}
        vocVerbe = {}
        for key in vocabulary:
            if vocabulary[key]['Type'] == "verbe":
                vocVerbe[key] = vocabulary[key]
            elif vocabulary[key]['Type'] == "phrase":
                vocPhrase[key] = vocabulary[key]
            elif vocabulary[key]['Type'] == "mot":
                if vocabulary[key]['Der-Die-Das'] =='' :
                    vocMot[key] = vocabulary[key]
                elif vocabulary[key]['Der-Die-Das'] !='' :
                    vocDerDieDasMot[key] = vocabulary[key]
                
        self.vocabulaire["vocabulaireBrut"]= vocabulary
        self.vocabulaire["vocPhrase"]={}
        self.vocabulaire["vocPhrase"]["elements"] = vocPhrase
        self.vocabulaire["vocMot"] = {}
        self.vocabulaire["vocMot"]["elements"] = vocMot
        self.vocabulaire["vocDerDieDasMot"] = {}
        self.vocabulaire["vocDerDieDasMot"]["elements"] = vocDerDieDasMot
        self.vocabulaire["vocVerbe"] = {}
        self.vocabulaire["vocVerbe"]["elements"] = vocVerbe

        # (nbrDerDieDas,nbrMots,vocDerDieDasMot,nbrPhrases,nbrVerbes) = self.countElementsVocabulaire(vocabulary)
        self.vocabulaire["vocDerDieDasMot"]['nbrElements'] = self.countElementsVocabulaire(vocDerDieDasMot)
        self.vocabulaire["vocMot"]['nbrElements'] = self.countElementsVocabulaire(vocMot)
        self.vocabulaire["vocPhrase"]['nbrElements'] = self.countElementsVocabulaire(vocPhrase) 
        self.vocabulaire["vocVerbe"]['nbrElements'] = self.countElementsVocabulaire(vocVerbe) 
        return

    def countElementsVocabulaire(self, vocabulary):
        nbrElements = 0
        for key in vocabulary: 
            nbrElements += 1
        return (nbrElements)

# CI-dessous, a supprimer lors du passage vers OOP, n'employer que "countElementsVocabulaire2()"
    # def countElementsVocabulaire(self):
    #     # Initialization du nombre d'éléments à exercer
    #     self.nbrMots = 0
    #     self.nbrPhrases = 0
    #     self.nbrVerbes = 0
    #     self.nbrDerDieDas = 0
    #     # On compte les mots et les phrase dans la page
    #     for key in self.vocabulaireBrut: 
    #         if self.vocabulaireBrut[key]['Type'] == 'mot':
    #             self.nbrMots +=1
    #             if self.vocabulaireBrut[key]['Der-Die-Das'] != '':
    #                 self.nbrDerDieDas +=1
    #         elif self.vocabulaireBrut[key]['Type'] == 'phrase':
    #             self.nbrPhrases +=1
    #         elif self.vocabulaireBrut[key]['Type'] == 'verbe':
    #             self.nbrVerbes +=1
    #     # print(self.nbrMots,self.nbrPhrases, self.nbrVerbes, self.nbrDerDieDas)
    #     return


    def addSettings(self, key, value):
        self.settings[key]=value
        return

    def printHello(self):
        print('hello')
        return

    def addChoix(self, key, value):
        self.choix[key]=value
        return

    def ecrire(self):
       
#à transformer:
# faire des dictionnaires: Mot, mot + derDieDaws, phrase ou verbe
# si mot ou phrase ou verbe écrire les éléments
# elif mot +derDieDas
#   ecrire derDieDas (que le der die ou das sans le mot ou le tout)
# si phrase ecrire phrase
# si verbe écrire verbe

        #Choisir le type d'éléments (phrase, mots verbes) avec ou sans aide...
        # if self.choix["quoiEcrire"] == "phrase":
        #     nombreElements = self.vocabulaire['vocPhrase']['nbrPhrases']
        #     elements = self.vocabulaire['vocPhrase']['elements']
        # elif self.choix["quoiEcrire"] == "verbe":
        #     nombreElements = self.vocabulaire['vocVerbe']['nbrVerbes']
        #     elements = self.vocabulaire['vocVerbe']['elements']
        # elif self.choix["quoiEcrire"] == "mot":
        #     if self.choix["derDieDas"] == "False":
        #         nombreElements = self.vocabulaire['vocMot']['nbrMots'] 
        #     else:
        #         nombreElements = self.vocabulaire['vocMot']['nbrDerDieDas']
        
        if not (self.choix["quoiEcrire"] == "mot" and self.choix["derDieDas"] == "True"): # cas standard
            if self.choix["quoiEcrire"] == "phrase":
                voc = self.vocabulaire['vocPhrase']['elements']
            if self.choix["quoiEcrire"] == "verbe":
                voc = self.vocabulaire['vocVerbe']['elements']
            if self.choix["quoiEcrire"] == "mot":
                voc = self.vocabulaire['vocMot']['elements']
        else: # exception cas: mot der die das
            if self.choix["quoiEcrire"] == "derDieDas":
                voc =self.vocabulaire['vocDerDieDasPhrase']['elements']
        
        # elif self.choix["quoiEcrire"] == "mot":
        #     if self.choix["derDieDas"] == "False":
        #         nombreElements = self.vocabulaire['vocMot']['nbrMots'] 
        #     else:
        #         nombreElements = self.vocabulaire['vocMot']['nbrDerDieDas']
        
        countElements = 0
        keyMotsDifficiles = []
        for key in voc:
            elementEtranger = self.vocabulaireBrut[key]['Mot en ALL']
            informationAEcrireEtrangerComplet = self.vocabulaireBrut[key]['Der-Die-Das'] + ' '+ self.vocabulaireBrut[key]['Mot en ALL']
            # informationAEcrireEtrangerDerDieDas = self.vocabulaire[key]['Der-Die-Das']
            if self.choix["derDieDas"] == "True": # choix.ecrireDerDieDas == True:
                elementEtranger = informationAEcrireEtrangerComplet
            elementFr = self.vocabulaireBrut[key]['Mot FR']
            reponseFausse = True
            tentative = 0
            if self.vocabulaireBrut[key]['Type'] == self.choix["quoiEcrire"]: #on filtre que les mots ou les phrases ou les verbes
                while reponseFausse:
                    reponse = input('[{countElements}/{nombreElements}], [{nbrEssai} essai/{nbrEssaiTot}] Ecrire le mot sans le déterminant: [{mot}] '.format(mot= elementFr, nbrEssai = tentative+1,nbrEssaiTot=self.settings["nombreTentativeMax"], countElements=countElements, nombreElements=nombreElements ))
                    # Vérifier la réponse ne contient pas de ", * etc....
                    tentative += 1
                    # if choix.ecrireDerDieDas == True:
                    #     reponseDerDieDas = reponse[:3]

                    if reponse == elementEtranger:
                        print('Bravo')
                        reponseFausse = False
                        evaluationReponse = 'juste'
                        playSoundGoodOOP(self.settings)
                    else:
                        evaluationReponse = 'faux'
                        playSoundBadOOP(self.settings)
                        if self.choix["aide"] == "True": #choix.ecrireMotPhraseAide:
                            # showError(informationAEcrireEtranger, reponse)
                            showErrorString(elementEtranger, reponse)

                    # # create the entry for the record
                    # repsonseLog = '{countElements}/{nombreElements}; {nbrEssai} tentative/{nbrEssaiTot}'.format(nbrEssaiTot=globalSettings.ecrireNombreTentativesMax, nbrEssai = tentative, countElements=countElements, nombreElements=nombreElements )
                    # entryLog = [globalSettings.currentDate, globalSettings.currentTime, choix.nomJoueur, choix.nomLangueChoisie, choix.nomVocChoisi, choix.nomPageChoisie, choix.typeExerciceChoisi, repsonseLog, evaluationReponse, informationAEcrireEtranger, reponse]
                    # # Log the attempt in a file
                    # recordTentative(entryLog, globalSettings)

                    if tentative == self.settings['nombreTentativeMax']: # globalSettings.ecrireNombreTentativesMax: #si le nombre de tentative max est atteint on arrête.
                        keyMotsDifficiles.append(key)                    
                        break
                print('[{motFR}] est [{motEtranger}]\n'.format(motEtranger=informationAEcrireEtrangerComplet, motFR = elementFr))
                countElements += 1
        return

    def trouver(self):
        pass

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
    elif choix.ecrireMotPhrase == "der-die-das":
        nombreElements = globalSettings.nbrDerDieDas
    # else:
    #     nombreElements = globalSettings.nbrPhrase

    for key in vocabulaireList:

        informationAEcrireEtranger = vocabulaireList[key]['Mot en ALL']
        informationAEcrireEtrangerComplet = vocabulaireList[key]['Der-Die-Das'] + ' '+ vocabulaireList[key]['Mot en ALL']
        informationAEcrireEtrangerDerDieDas = vocabulaireList[key]['Der-Die-Das']
        if choix.ecrireDerDieDas == True:
            informationAEcrireEtranger = informationAEcrireEtrangerComplet
        informationAEcrireFR = vocabulaireList[key]['Mot FR']
        reponseFausse = True
        tentative = 0
        if vocabulaireList[key]['Type'] == choix.ecrireMotPhrase: #on ne fait que les mots ou les phrases ...
            # ecrireDerDieDas
            # os.system('cls' if os.name == 'nt' else 'clear') #Clear terminal screen 
            while reponseFausse:
                reponse = input('[{countElements}/{nombreElements}], [{nbrEssai} essai/{nbrEssaiTot}] Ecrire le mot sans le déterminant: [{mot}] '.format(mot= informationAEcrireFR, nbrEssai = tentative+1,nbrEssaiTot=globalSettings.ecrireNombreTentativesMax, countElements=countElements, nombreElements=nombreElements ))
                # Vérifier la réponse ne contient pas de ", * etc....
                tentative += 1
                # if choix.ecrireDerDieDas == True:
                #     reponseDerDieDas = reponse[:3]

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

def ecritureChoixTypeExercice(vocabulaireList, choix, globalSettings):
    sorted(vocabulaireList)
    print('Ecrire des mots ou des phrases ?')
    optionChoisie = choisirElement(['mot', 'mot avec aide','der-die-das', 'verbe','verbe avec aide', 'phrase', 'phrase avec aide'])
    if optionChoisie == 'mot':
        choix.ecrireMotPhrase = 'mot'
        choix.ecrireDerDieDas = False
        choix.ecrireDerDieDas = False
        choix.ecrireMotPhraseAide = False
    elif optionChoisie == 'mot avec aide':
        choix.ecrireMotPhrase = 'mot'
        choix.ecrireDerDieDas = False
        choix.ecrireMotPhraseAide = True
    elif optionChoisie == 'der-die-das':
        choix.ecrireMotPhrase = 'mot'
        choix.ecrireDerDieDas = True
        choix.ecrireMotPhraseAide = False
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
