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