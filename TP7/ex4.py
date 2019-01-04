# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 15:47:59 2018

@author: vgrison
"""

def estCorrecte(s):
    chiffres = "0123456789"
    var=0
    for carac in s:
        if(len(s)>=8) and (carac in chiffres):
            var=var+1
        else:
            ()
    if (var!=0):
        print("ui")
    else:
        print("non")

s=str(input("dopsqdpqsdk :"))
a=estCorrecte(s)
print(a)