

from tkinter import *
def clic():
    print("J'ai cliqué sur le bouton !")
def afficher():
    t=entree.get()
    print("Vous avez saisi : ",t)
    
fen=Tk()
texte1=Label(fen,text="Bonjour !",fg="pink" ,bg="white" ,font="courrier")
texte1.grid(row=0,column=0,columnspan=2)
texte1=Label(fen,text="Saisir un nombre",fg="pink" ,bg="white" ,font="courrier")
texte1.grid(row=1,column=0)
bou=Button(fen,text="Quitter",command=fen.destroy)
bou.grid(row=2,column=2)
bou2=Button(fen,text="Cliquer ici",command=clic)
bou2.grid(row=0,column=2)
entree=Entry(fen)
entree.grid(row=1,column=1)
bou3=Button(fen,text="Valider",command=afficher)
bou3.grid(row=1,column=2)


fen.mainloop()