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

class ExerciceTime:
    """Represent a vocabulary exercice 
    
    attributes: vocabulary
    """
    def __init__(self):
        # self.vocabulary = vocabulary
        pass
    
    # def displayVoc(self):
    #     print('Vocabulary: ')

    def startTime(self):
        self.maintenant = datetime.datetime.today()

    def stopTime(self):
        self.stop = datetime.datetime.today()

    def deltaTime(self):
        self.delta = self.stop - self.maintenant
        print('delta sec: ' + str(self.delta.seconds))
        print('hello')

    # # Initializer / Instance Attributes
    # def __init__(self, name):
    #     self.name = name
    #     # self.age = age

# exercice1 = ExerciceVoc('vocAnglais')
# exercice1 = ExerciceVoc('juice')
# print(exercice1)
# texte = 'hello'
# exercice2 = ExerciceVoc(texte)
# exercice1.displayVoc()
# exercice1.startTime()

exercice1Time = ExerciceTime()
exercice1Time.startTime()
input('wait')
exercice1Time.stopTime()
exercice1Time.deltaTime()
# print('delta min: {min} et sec: {sec}'.format(min=0, sec = delta.seconds))
