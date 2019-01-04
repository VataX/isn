# -*- coding: utf-8 -*-

def decodbin(s):
    n=0
    for i in range(len(s)):
        n= n + int(s[i])*2**(len(s)-i-1)
    return n

s=str(input("sofodsf: "))
a=decodbin(s)
print(a)