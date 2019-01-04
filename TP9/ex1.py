# -*- coding: utf-8 -*-
annuaire=[["Bonnet","Nicolas","0102030405"],
       ["Dupont","Aline","0106070809"], 
       ["Garnier","Romain","0102101112"],
       ["Lecomte","Raphaël","0103202122"],
       ["Martin","Pauline","0103353637"],
       ["Simon","Marie","0104050607"]]


def recherche(nom,prenom):
    for i in range(len(annuaire)):
        if nom == annuaire[i][0] and prenom == annuaire[i][1]:
            return i
    return -1

def rechercheTel(nom,prenom):
    for i in range(len(annuaire)):
        if nom == annuaire[i][0] and prenom == annuaire[i][1]:
            return annuaire[i][2]
    return "Incconu"    
    
def annuaireInverse(numéro):
    for i in range(len(annuaire)):
        if numéro == annuaire[i][2]:
            return annuaire[i][0] + annuaire[i][1]
    return "Numéro incconu"

def ajoute():
    nom=input("nom ? ")
    prenom=input("prénom ? ")
    numéro=input("numéro ? :")
    a=recherche(nom,prenom)
    if a==-1:
        annuaire.append([nom,prenom,numéro])
    else:
        annuaire[a][2]=numéro
    
def supprime(nom,prenom):
    a=recherche(nom,prenom)
    if a==-1:
        print("erreur")
    else:
        del annuaire[a]
