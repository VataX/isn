# -*- coding: utf-8 -*-
classes=[["2A","11h30"],["2B","11h30"],["2C","11h30"],["2D","11h30"],["2E","11h30"],["2F","11h30"],["2G","11h30"],["2H","11h30"],["2I","11h30"],["1L1","11h30"],["1L2","11h30"],["1ES1","11h30"],["1ES2","11h30"],["1ES3","12h30"],["1S1","12h30"],["1S2","12h30"],["1S3","12h30"],["1S4","12h30"],["1S5","12h30"],["TL1","12h30"],["TL2","12h30"],["TES1","12h30"],["TES2","12h30"],["TES3","12h30"],["TS1","12h30"],["TS2","12h30"],["TS3","12h30"],["TS4","12h30"],["TS5","12h30"]]
#classes=[["2A","11h30"],["2B","11h30"],["2C","11h30"],["2D","11h30"],["2E","11h30"],["2F","11h30"],["2G","11h30"],["1L1","11h30"],["1L2","11h30"],["1ES1","11h30"],["1ES2","11h30"],["1S1","12h30"],["1S2","12h30"],["1S3","12h30"],["1S4","12h30"],["TL1","12h30"],["TL2","12h30"],["TES1","12h30"],["TES2","12h30"],["TS1","11h30"],["TS2","11h30"],["TS3","11h30"],["TS4","11h30"]]
#classes=[["2A","11h30"],["2B","11h30"],["2C","11h30"],["2D","11h30"],["2E","11h30"],["2F","11h30"],["2G","11h30"],["2H","11h30"],["2I","11h30"],["2J","12h30"],["2K","12h30"],["2L","12h30"],["1L1","11h30"],["1L2","11h30"],["1L3","12h30"],["1ES1","11h30"],["1ES2","11h30"],["1ES3","12h30"],["1ES4","12h30"],["1S1","12h30"],["1S2","12h30"],["1S3","12h30"],["1S4","12h30"],["1S5","12h30"],["TL1","12h30"],["TL2","12h30"],["TES1","12h30"],["TES2","12h30"],["TES3","12h30"],["TES4","12h30"],["TS1","12h30"],["TS2","12h30"],["TS3","12h30"],["TS4","12h30"],["TS5","12h30"],["TS6","12h30"]]

from math import*

def vérifier():
    nb=0
    for i in classes:
        if i[1]=="11h30":
            nb=nb+1
    if 0.4<=nb/len(classes) and nb/len(classes)<=0.6:
        print("Bonne répartition des classes")
    elif 0.4<nb/len(classes):
        print("Revoir la répartition ! Il faut plus de classes à 11h30")
        print("Il faut au moins", ceil(0.4*len(classes)), "classes à 11h30")
    else:
        print("Revoir la répartition ! Il faut moins de classes à 11h30")
        print("Il faut max", ceil(0.6*len(classes)), "classes à 11h30")
        
        
vérifier()