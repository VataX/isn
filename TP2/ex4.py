# -*- coding: utf-8 -*-

temp=float(input("Saisissez une température: "))
type_temp=str(input("Saisir l'unité de cette température (F pour fahrenhiet,C pour celsius): "))

if (type_temp=="c") or (type_temp=="C"):
    print("La température vaut", temp*1.8+32, "degrés farenheit.")
elif (type_temp=="f") or (type_temp=="F"):
    print("La température vaut", (temp-32)/1.8, "degrés celcius.")
else:  
    print("Vous n'avez pas saisi une unité valide.")
    