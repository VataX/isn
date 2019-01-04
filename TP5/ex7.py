# -*- coding: utf-8 -*-

def syracuse(N,n):
    for i in range(n):
        if(N%2==0):
            N=N/2
            print(N)
        else:
            N=3*N+1
            print(N)

def vol(N):
    count=0
    while (N!=1):
        if(N%2==0):
            N=N/2
            print(N)
            count=count+1
        else:
            N=3*N+1
            print(N)
            count=count+1
    print("Temps de vol le plus court :",count)

N=int(input("Choisissez un N: "))
n=int(input("Choisissez un n: "))

vol(N)