# -*- coding: utf-8 -*-
from turtle import*

longueur=float(input("Saisissez la longueur: "))

if (longueur>0):
    color("red")
    forward(longueur)
    right(144)
    forward(longueur)
    right(144)
    forward(longueur)
    right(144)
    forward(longueur)
    right(144)
    forward(longueur)
else:
    print("Erreur, la longueur est  négative.")