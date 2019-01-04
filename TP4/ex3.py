# -*- coding: utf-8 -*-

code=int(input("Entrez votre code secret :"))
codeconf=int(input("Confirmez votre code secret :"))

while(code!=codeconf):
    codeconf=int(input("Erreur, les deux codes ne correspondent pas. Veuillez reconfirmer votre code :"))
print("Merci !")