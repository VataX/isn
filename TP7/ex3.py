# -*- coding: utf-8 -*-

def inverse(s):
    x=""
    for i in s:
        x=i+x
    return x
    
def palindrome(s):
    if(inverse(s)==s):
        print("oui")
    else:
        print("non")

s=str(input("Saisissez une phrase :"))
a=palindrome(s)
print(a)