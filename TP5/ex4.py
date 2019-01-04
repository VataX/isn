
def prixTTC(HT,taux):
    return HT*(1+taux/100)
d=prixTTC(100,10)
print(d)
