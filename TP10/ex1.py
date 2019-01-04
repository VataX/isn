
def binaire(n):
    s=""
    if (n==0):
        return "0"
    else:
        while (n!=0):
            reste=n%2
            s=str(reste) + s
            n=n//2
    return s

n=int(input("Saisissez un entier: "))
a=binaire(n)
print(a)