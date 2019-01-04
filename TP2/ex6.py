# -*- coding: utf-8 -*-

from math import*

type_calcul=str(input("Quel calculer voulez-vous effectuer ? Appuyez sur P pour calculer le périmète d'un cercle ou sur A pour calculer le rayon d'un disque: "))
rayon=float(input("Saisissez la valeur rayon: "))

if rayon<0:
    print("Erreur: le rayon ne peut pas être négatif")
else:
    if (type_calcul=="p") or (type_calcul=="P"):
        print("L'aire vaut", 2*pi*rayon)
    elif (type_calcul=="a") or (type_calcul=="A"):
        print("L'aire vaut", pi*(rayon**2))
    else: 
        print("Erreur: type de calcul invalide")