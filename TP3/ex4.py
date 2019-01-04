# -*- coding: utf-8 -*-
t=0

for i in range(1,65):
    t= t+ 2**(i-1)
    print(2**(i-1), "grains sur la case", i)
print(t, "grains de riz au total")