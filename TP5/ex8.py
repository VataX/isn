# -*- coding: utf-8 -*-


from turtle import*
from math import*


def carré(c,couleur,angle):
    color(couleur)
    forward(c)
    left(90)
    forward(c)
    left(90)
    forward(c)
    left(90)
    forward(c)
    left(90)

def figure(c, couleur):
    for i in range(20):
        carré(c, couleur, angle)
        forward(c/4)
        left(18.435)
        c=sqrt(5/8)*c
        
c=int(input("c? "))
couleur=str(input("couleur ? "))
angle=float(input("angle ? "))
figure(c, couleur)