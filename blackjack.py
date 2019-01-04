# -*- coding: utf-8 -*-
from random import*

jeu=[2,3,4,5,6,7,8,9,10,11]*4 # Création de la liste jeu, qui contient toutes les valeurs de cartes possibles
main, main_joueur, main_ordinateur, carte_tiree = [], [], [], [] # Création des mains

def ajout_carte(main): # Permet de tirer une carte
    carte_tiree = choice(jeu) # Place une carte dujeu au hasard à la liste carte_tiree
    main.append(carte_tiree) # Ajoute la carte tirée à la main
    jeu.remove(carte_tiree) # Supprime la carte tirée du jeu

def tirage(): # Tirage de deux cartes au hasard en début de partie
    cartes = []
    for i in range(2): # Ajout de deux cartes à la liste cartes
        ajout_carte(cartes)
    if (cartes[len(cartes)-1] == 11) and (cartes[len(cartes)-2] == 11): # Si deux as sont tirés, un prend la valeur 1
        cartes[len(cartes)-2] = 1
    else:
        ()
    return cartes

def total(main): # Calcul de la valeur total d'une main
    if sum(main) > 21 and 11 in main: # Si la somme est supérieure à 21 et qu'un as est préent dans la main, il prend la valeur 1
        for elt in range(len(main)-1):
            if main[elt] == 11:
                main[elt] = 1

    return sum(main)

def jouer(): # Assurer le fonctionnement d'une partie
    # Mise en place de la partie
    main_joueur.append(tirage()[0]) # Ajout de deux cartes à la main du joueur
    main_joueur.append(tirage()[1])
    main_ordinateur.append(tirage()[0]) # Ajout de deux cartes à la main de l'ordinateur
    main_ordinateur.append(tirage()[0])

    if total(main_joueur) == 21: # Cas du backjack: la main tirée au départ vaut 21
        print("BlackJack ! Main du joueur:", main_joueur)
        print("Main de l'ordinateur:", main_ordinateur)
        encore = str(input("Voulez-vous rejouer ? oui/non "))
        if (encore == 'oui'):
            rejouer()
        else:
            exit
    elif total(main_ordinateur) == 21: # Cas du blackjack pour l'ordinateur
        print("BlackJack de l'ordinateur ! Main de l'ordinateur:", main_ordinateur)
        print("Main du joueur:", main_joueur)
        encore = str(input("Voulez-vous rejouer ? oui/non "))
        if (encore == 'oui'):
            rejouer()
        else:
            exit
    else: # Cas d'une partie 'classique'
        print("Main du joueur:",main_joueur)
        print("Première carte de l'ordinateur:",main_ordinateur[0])


        # Jeu après la pioche de départ
        choix_joueur = str(input("Voulez-vous tirer une nouvelle carte ? oui/non ")) # Le joueur peut continuer à piocher des cartes tant que la valeur de sa main est inférieure à 21
        while choix_joueur == "oui" and total(main_joueur) < 21 :
            ajout_carte(main_joueur)
            if total(main_joueur) <  21:
                print('Main du joueur:', main_joueur, '(somme:', total(main_joueur),")")
                choix_joueur = str(input("Voulez-vous tirer une nouvelle carte ? oui/non "))
            elif total(main_joueur) == 21:
                print("Blackjack, gagné !")
                encore = str(input("Voulez-vous rejouer ? oui/non "))
                if (encore == 'oui'):
                    rejouer()
                else:
                    exit
            else:
                choix_joueur = 'non'
                print("Perdu !")
                print('Main du joueur', main_joueur, '(somme:', total(main_joueur),')')

        while total(main_ordinateur) < 17: # L'ordinateur continue de piocher des cartes tant que la valeur de sa main est inférieur à 17
            ajout_carte(main_ordinateur)

        # Résultats
        if total(main_ordinateur) >  21 and total(main_joueur) < 21: # Victoire du joueur si la valeur de la main de l'ordinateur est supérieure à 21
            print("Gagné !")
            print("Main de l'ordinateur:", main_ordinateur, '(somme:', total(main_ordinateur),')')

        if total(main_joueur) < 21 and total(main_ordinateur) < 21: # Victoire du joueur dont la valeur de la main est la plus proche de 21
            if total(main_joueur) < total(main_ordinateur):
                print("Perdu !")
                print('Main du joueur:', main_joueur, '(somme:', total(main_joueur),")")
                print("Main de l'ordinateur:", main_ordinateur, '(somme:', total(main_ordinateur),')')
            elif total(main_joueur) == total(main_ordinateur):
                print("Egalité !")
                print('Main des joueurs:', main_joueur, main_ordinateur, '(somme:', total(main_joueur),")")
            else:
                print("Gagné !")
                print('Main du joueur:', main_joueur, '(somme:', total(main_joueur),")")
                print("Main de l'ordinateur:", main_ordinateur, '(somme:', total(main_ordinateur),')')

        encore = str(input("Voulez-vous rejouer ? oui/non ")) # Possibilité de relancer une partie
        if (encore == 'oui'):
            rejouer()
        else:
            exit

def rejouer(): # Relancer une partie
    # Remise à zéro des mains
    del main_joueur[:]
    del main_ordinateur[:]
    del carte_tiree[:]
    jeu=[2,3,4,5,6,7,8,9,10,11]*4 # Remise à zéro du jeu
    jouer() # Lancement d'une partie


jouer() # Lancement d'une partie
