
# -*- coding: utf-8 -*-

from turtle import*


longueur=float(input("Saisissez une longueur pour la croix: "))
nb=float(input("Saisissez un nb pour la croix: "))
i=0
color("red")
while(i<=nb):
    speed(1)
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
    right(360/n)
    up()
    goto(longueur/2,longueur/2)
    down()
    i=i+1
done()

