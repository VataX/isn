# -*- coding: utf-8 -*-

poids=float(input("Quel est le poids de votre lettre en grammes ? "))
type_lettre=float(inpute("Quel est le type de lettre ? V pour verte, P pour prioritaire, E pour Ecopli "))

if (poids<=20):
    if (type_lettre=="V") or (type_lettre=="v"):
        print("0,80€")
    if (type_lettre=="P") or (type_lettre=="p"):
        print("0,95€")
    if (type_lettre=="V") or (type_lettre=="v"):
        print("0,78€")
elif (poids<=100):
    if (type_lettre=="V") or (type_lettre=="v"):
        print("1.60€")
    if (type_lettre=="P") or (type_lettre=="p"):
        print("1.90€")
    if (type_lettre=="V") or (type_lettre=="v"):
        print("1.56€")
else (poids<=250):
    if (type_lettre=="V") or (type_lettre=="v"):
        print("1.60€")
    if (type_lettre=="P") or (type_lettre=="p"):
        print("1.90€")
    if (type_lettre=="V") or (type_lettre=="v"):
        print("1.56€")