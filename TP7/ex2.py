# -*- coding: utf-8 -*-

def compteMots(s):
    count=1
    for espace in s:
        if(espace==" "):
            count=count+1
    return count
    
s=str(input("Saisissez une phrase :"))
a=compteMots(s)
print(a)