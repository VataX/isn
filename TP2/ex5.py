# -*- coding: utf-8 -*-

poids=float(input("Quel est votre poids en kilogrammes ?: "))
taille=float(input("Quelle est votre taille en mètres ?: "))

IMC= poids/(taille**2)

if(IMC<18.5):
    print("Votre IMC est de :", IMC, "Vous êtes en sous poids ! Mangez !")
elif(IMC>25):
    print("Votre IMC est de :", IMC, "Vous êtes en surpoids ! Faîtes du sport !")
else:
    print("Votre IMC est de :", IMC, "Vous avez une corpulence normale.")