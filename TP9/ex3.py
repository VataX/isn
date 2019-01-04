# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 15:45:09 2018

@author: vgrison
"""
from random import*

def grille():
    listegrille=[]
    for i in range(5):
        if i==5:
            listegrille.append(randint(1,10))
        else:
            listegrille.append(randint(1,50))
    return listegrille
    
def plusieursGrilles(nb):
    plsgrilles=[]
    for j in range(nb):
        a=grille()
        plsgrilles.append(a)
    return plsgrilles
 
nb=int(input("Cb de grilles? "))
x=plusieursGrilles(nb)
print(x)