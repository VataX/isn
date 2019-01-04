# -*- coding: utf-8 -*-

from turtle import*

n=int(input("Choisissez un nb :"))
i=0

color("red")
speed(5000000000000000000)
while(i<=n):
    width(1)
    circle(250)
    right(360/n)
    i=i+1
done()

