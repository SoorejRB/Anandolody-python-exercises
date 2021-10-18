# Problem 37: Write a function valuesort to sort values of a dictionary based on the key.

import sys

def valuesort(x):
    a=x.items()
    a.sort(key=lambda x:x[0])
    i=0
    c=[]
    while i<len(a):
        c.append(a[i][1])
        i=i+1
    return c
print(valuesort({'x':1,'y':2,'a':4,'k':3}))