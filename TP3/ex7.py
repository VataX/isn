# -*- coding: utf-8 -*-
nb_mineur=0
age_saisi=0
nb_age=int(input("Combien d'âges souhaitez-vous rentrer ? "))

for i in range(1, nb_age+1):
    age_saisi= int(input("Saisissez un âge: "))
    if (age_saisi < 18):
        nb_mineur= nb_mineur + 1
print(nb_mineur, "mineurs")