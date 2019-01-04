# -*- coding: utf-8 -*-

def codage(s,mot):
    chaine=""
    lettre=0
    for carac in s:
        chaine=carac+mot[lettre]
        lettre=lettre+1
        if(lettre>=len(s)-1):
            lettre=0
        else:
            ()
    return chaine
    
s=str(input("Saisissez une phrase :"))
mot=str(input("Saisissez une phrase :"))
a=codage(s,mot)
print(a)

## MARCHE PAS