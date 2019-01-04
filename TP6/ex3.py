# -*- coding: utf-8 -*-

from random import *
from tkinter import *
def afficher():
    t=entree.get()
    print("Vous avez saisi : ",t)

def valider():
    nbessais= nbessais+1
    

n = randint(1,100)
nbessais=0


fen=Tk()
texte1=Label(fen,text="Saisir un nombre",fg="black" ,bg="white" ,font="courrier")
texte1.grid(row=0,column=0)
entree=Entry(fen)
entree.grid(row=0,column=1)
bou3=Button(fen,text="Valider",command=afficher)
bou3.grid(row=0,column=2)
texte1=Label(fen,text="A vous de jouer !",fg="black" ,bg="white" ,font="courrier")
texte1.grid(row=1,column=0,columnspan=2)
fen.mainloop()