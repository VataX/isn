
# -*- coding: utf-8 -*-

from turtle import*


longueur=float(input("Saisissez une longueur: "))

if (longueur>0):
    color("red")
    forward(longueur/2)
    left(90)
    forward(longueur)
    right(90)
    forward(longueur/2)
    up()
    goto(0,longueur)
    down()
    right(90)
    forward(longueur/2)
    left(90)
    forward(longueur)
    right(90)
    forward(longueur/2)

    
else:
    print("Erreur, la longueur est  négative.")