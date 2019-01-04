
jour=int(input("Saisissez un jour: "))
mois=int(input("Saisissez un mois: "))

if (jour<20) and (mois<=3):
    print("C'est l'hiver")
elif (jour<21) and (mois<=6):
    print("C'est le printemps")
elif (jour<23) and (mois<=9):
    print("C'est l'été")
else:
    print("C'est l'hiver")
    