# -*- coding: utf-8 -*-

from random import*
n=randint(1,100)

u=int(input("Chosissez un entier entre 1 et 100 :"))
e=1

while(u!=n):
    if (u<n):
        print("C'est plus")
        u=int(input("Chosissez un nouveau nombre :"))
        e=e+1
    elif (u>n):
        print("c'est moins")
        u=int(input("Chosissez un nouveau nombre :"))
        e=e+1
print("Vous avez gagné en", e, "essais" )