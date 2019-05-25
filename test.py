import time
import winsound # Son, bruitage 
import os #for terminal screen clearing
from random import shuffle
import csv #for statistics logs
import random
import difflib # https://pymotw.com/2/difflib/ 
# from difflib_data import *
from pprint import pprint
import sys
import datetime
from func import *
from collections import Counter
import operator #for sorting dict by value
import collections

keyMotsDifficiles = ['6', '6', '3'] #for debug only 
statErreurKeyFreq = Counter(keyMotsDifficiles) # Key : freq

sorted_freq = sorted(statErreurKeyFreq, reverse = True)



print('*** Tes pires ennemis ***')
for tempKey in sorted_freq:
    # for tempKey in sorted_Errors:
        reponse = motsDifficilesEtFrequence['motsDifficiles'][tempKey]['Der-Die-Das'] + ' ' + motsDifficilesEtFrequence['motsDifficiles'][tempKey]['Mot en ALL']
        print('{frequenceFaux} x faux: {indice} = {reponse}'.format(frequenceFaux=motsDifficilesEtFrequence['frequenceErreur'][tempKey], indice = motsDifficilesEtFrequence['motsDifficiles'][tempKey]['Mot FR'], reponse = reponse))


motsDifficilesEtFrequence={}
motsDifficilesEtFrequence['frequenceErreurs'] = {}
# motsDifficilesEtFrequence['frequenceErreurs']= {Counter({'1': 2, '3': 1}), 'motsDifficiles': {'1': {...}, '3': {...}}}
motsDifficilesEtFrequence['frequenceErreurs']= {'1': 1, '3': 4}
sorted_Errors = sorted(motsDifficilesEtFrequence['frequenceErreurs'].items(), key=operator.itemgetter(1), reverse = True)
# Counter = {'6': 2, '10': 1}
Counter = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_Errors = sorted(Counter.items(), key=operator.itemgetter(1), reverse = True)
print('*** Tes pires ennemis ***')
# for tempKey in motsDifficilesEtFrequence['motsDifficiles']:


# sorted_dict = collections.OrderedDict(sorted_Errors)

for tempKey in sorted_Errors:
    pass

z = ['blue', 'red', 'blue', 'yellow', 'blue', 'red']
stat = Counter(z)


val = 'asdf'
try:
    int(val)
    pass
except:
    pass
# class ExerciceClass:
#     """Exercice d'écriture
#     """
#     def __init__(self, vocabulaire):
#         self.vocabulaire = vocabulaire
    
#     def printHello(self):
#         print('hello')

# voca={"1":"hello"}
# exercice1 = ExerciceClass(voca)
# exercice1.printHello()
class SettingGlobal(object):
    """Global class to hold the settings"""
globalSettings = SettingGlobal()
globalSettings.soundActive = True

# def playSoundGood():
# # def playSoundGood(globalSettings):
#     global globalSettings
#     if globalSettings.soundActive == True:
#         winsound.PlaySound(globalSettings.goodSound, winsound.SND_FILENAME)
#     return

playSoundGood()