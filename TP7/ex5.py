# -*- coding: utf-8 -*-

def sansEspace(s):
    chaine=""
    for carac in s:
        if(carac==" "):
            ()
        else:
            chaine=chaine+carac
    return chaine
    
s=str(input("Saisissez une phrase :"))
a=sansEspace(s)
print(a)