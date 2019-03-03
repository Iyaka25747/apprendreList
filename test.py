
fin = input("Enter text: ")
print("Input: " + fin)

recordFile = "test.txt"
myFile = open(recordFile, 'w')
print("Enregistrement des calculs dans {fichier}".format(fichier = recordFile ))
myFile.write("input: " + fin)
myFile.close()
print("Fin de l'enregistrement")

