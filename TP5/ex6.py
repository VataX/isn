
# -*- coding: utf-8 -*-

from random import *

def unepartie():
    po=0
    pj=0
    nom=str(input("Nom ? "))
    choix=int(input("Choix ? "))
        
    if (choix==1):
        print(nom," a choisi pierre")
    if (choix==2):
        print(nom,"a choisi feuille")
    if (choix==3):
        print(nom,"a choisi ciseaux")
    
    choixo=randint(1,3)
    if (choixo==1):
        print("L'ordinateur a choisi pierre")
    if (choixo==2):
        print("L'ordinateur a choisi feuille")
    if (choixo==3):
        print("L'ordinateur a choisi ciseaux")
    
    if (choix==1):
        if (choixo==1):
            print("Egalité")
        elif (choixo==2):
            print("Perdu")
        else:
            print("Gagné")
    if (choix==2):
        if (choixo==2):
            print("Egalité")
        elif (choixo==3):
            print("Perdu")
        else:
            print("Gagné")
    if (choix==3):
        if (choixo==3):
            print("Egalité")
        elif (choixo==1):
            print("Perdu")
        else:
            print("Gagné")

    encore=str(input("Encore une partie ? (o pour oui et n pour non) "))
    if(encore=="o"):
        unepartie()
    else:
        ()

  
unepartie()
    
