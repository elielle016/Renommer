import os
from os import listdir
from os.path import isfile, join

dir = os.getcwd()
masque = "super_fichier_"

fichiers = [f for f in listdir(dir) if isfile(join(dir, f))]

for i in range (len(fichiers)):
    os.rename(fichiers[i], masque+str(i+1))
print("les fichiers ont été renommés avec succès")