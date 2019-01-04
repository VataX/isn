
def compteCar(s,c):
    count=0
    for car in s:
        if(car==c):
            count=count+1
    return count


ch=str(input("Saisissez une phrase: "))
ca=str(input("Saisissez une lettre :"))
a=compteCar(ch,ca)
print(a)