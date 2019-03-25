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

class ExerciceVoc:
    """Represent a vocabulary exercice 
    
    attributes: vocabulary
    """
    def __init__(self, vocabulary):
        self.vocabulary = vocabulary
    
    def displayVoc(self):
        print('Vocabulary: ')

    # # Initializer / Instance Attributes
    # def __init__(self, name):
    #     self.name = name
    #     # self.age = age

# exercice1 = ExerciceVoc('vocAnglais')
exercice1 = ExerciceVoc('juice')
print(exercice1)
texte = 'hello'
exercice2 = ExerciceVoc(texte)
exercice1.displayVoc()