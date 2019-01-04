from random import *

def aleat(n):
    liste=[]
    for i in range(n):
        liste.append(randint(0,100))
    return liste
    
def supDix(liste):
    nbsupdix=0
    for j in range(len(liste)):
        if(liste[j] >=10):
            nbsupdix=nbsupdix+1
    return nbsupdix

n=int(input("Saisir un entier: "))
a=aleat(n)
print(a)
b=supDix(a)
print(b)
