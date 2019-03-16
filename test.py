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

text1 = '''1. Beautiful is better than ugly.
2. Explicit is better than implicit.
3. Simple is better than complex.
4. Complex is better than complicated.
'''.splitlines(1)
text2 = '''1. Beautiful is better than ugly.
3. Simple is better than complex.
4. Complicated is better than complex.
5. Flat is better than nested.
'''.splitlines(1)

text1 = 'Herzlichen Glückwunsch zum Geburtstag!'
text2 = 'Herzlichen Gloukwunsch zum Geburtstag!uuu'
text1 = [text1]
text2 = [text2]


d = difflib.Differ()    
result = list(d.compare(text1, text2))
print(type(result))
pprint(result)
print('\n+++++++++++++++\n')
for text in result:
    text = text.strip()
    print(text)
pass
test = '   spacious^^\n'.rstrip()
pass