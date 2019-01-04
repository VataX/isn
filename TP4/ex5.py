# -*- coding: utf-8 -*-
j=20
m=0
while(j<= 31 ):
    for m in range(1,13):
        if (m==2) and (j<29):
            print(str(j)+"/"+"0"+str(m)+"/"+str(j)+"0"+str(m))
        elif (m==2) and (j>=29):
            print()
        elif (m<10) and (m%2!=0):
            print(str(j)+"/"+"0"+str(m)+"/"+str(j)+"0"+str(m))

        elif (m<10) and (m%2==0) and (j<31):
            print(str(j)+"/"+"0"+str(m)+"/"+str(j)+"0"+str(m))
        elif (m>=10) and (m%2!=0):
            print(str(j)+"/"+str(m)+"/"+str(j)+str(m))
        elif (m>=10) and (m%2==0) and (j<31):
            print(str(j)+"/"+str(m)+"/"+str(j)+str(m))
        else:
            print()
        m=m+1
    j=j+1