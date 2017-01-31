# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 18:34:58 2017

@author: herilalaina, fidele
"""

import os
import pickle as pkl
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

# Load ML model
clf = pkl.load(open("model.pkl", "rb"))

def affiche_entete(erreur = ''):
    os.system("clear")
    print "\n\n\t\t***********************************************"
    print "\t\t**************** WikiOrNot ********************"
    print "\t\t***********************************************"
    print "\t\tHerilalaina                              Fidele\n\n"
    
    print "Voulez vous savoir si une phrase viens d'un source wikipedia ou d'un journal ?"
    if len(erreur) > 1 :
        print "###### ERROR : " + erreur + " ######"
    nom_fichier = raw_input('Entrer le nom du fichier qui contient la phrase :  ')
    return nom_fichier

def lire_nom_fichier():
    # Demander le nom du fichier contenant la phrase
    sortir_boucle_fichier = False
    nom_fichier = None
    erreur = ''
    while(not sortir_boucle_fichier):
        nom_fichier = affiche_entete(erreur)
        if os.path.isfile(nom_fichier):
            sortir_boucle_fichier = True
            erreur = ""
        else:
            erreur = "impossible de lire le fichier " + nom_fichier

    return nom_fichier

def predire(nom_fichier):
    # Prepare file
    os.system("sh convert-text.sh " + nom_fichier + " out.csv")
    
    # Load out.csv
    X_test = pd.read_csv("out.csv", sep=" ")
    
    res = clf.predict(X_test)
    
    if res[0] == 1:
        print "\n\n>>>>>>>> Cette phrase vient de wikipedia <<<<<<<<< \n\n"
    else:
        print "\n\n>>>>>>>> Cette phrase vient de journal <<<<<<<<< \n\n"

sortir = False
while(not sortir):
    nfichier = lire_nom_fichier()    
    predire(nfichier)
    r = raw_input("Voulez vous réessayer ? (y/n): ")
    if r == "n":
        break
print "\n\n Bye bye. A la prochaine ;) \n\n"
print "\t\t***********************************************\n\n"
    
    