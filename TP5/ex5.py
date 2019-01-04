
from random import *

def lancerDé():
    de=0
    nblancer=0
    while (de!=6):
        de=randint(1,6)
        nblancer=nblancer+1
    return nblancer


pari=int(input("Sur combien de lancers pariez vous ? "))
lancerDé()
if (pari==nblancer):
    print(nblancer, "lancers, c'est gagné")
else:
    print(nblancer, "lancers, c'est perdu")





