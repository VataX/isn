from turtle import*


longueur=float(input("Saisissez la longueur du carré: "))

if (longueur>0):
    color("red")
    forward(longueur)
    left(90)
    forward(longueur)
    left(90)
    forward(longueur)
    left(90)
    forward(longueur)
else:
    print("Erreur, la longueur est  négative.")
