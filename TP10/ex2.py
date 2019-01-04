
def hexa(n):
    s=""
    if (n==0):
        return "0"
    else:
        while (n!=0):
            reste=n%16
            if(reste==10):
                reste="A"
            if(reste==11):
                reste="B"
            if(reste==12):
                reste="C"
            if(reste==13):
                reste="D"
            if(reste==14):
                reste="E"
            if(reste==15):
                reste="F"
            s=str(reste) + s
            n=n//16
    return s

n=int(input("Saisissez un entier: "))
a=hexa(n)
print(a)