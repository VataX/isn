# -*- coding: utf-8 -*-

r=int(input("Combien font 7 fois 8 ? "))
i=1
while(r!=56):
    print(r)
    i=i+1
    r=int(input("Erreur, veuillez saisir une nouvelle valeur :"))
print(r)
print("Bonne réponse ! Vous l'avez trouvé en", i, "essais")
    