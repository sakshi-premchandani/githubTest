# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 20:54:37 2023

@author: DELL
"""

#list dissimilar types of data
a=[1,2,3,10,11]
print(a[0])
print(len(a))
suma=0
for i in range(len(a)):
    suma=suma+a[i]
print(suma)
#find max element
maxi=a[0]
for i in range(len(a)):
    if(maxi<a[i]):
        maxi=a[i]
print(maxi)     
a.append(21)  # for lastinsert
#for first index inserion shift elements then insert
#list of list
b=[[1,2,4],[4,5],[8,9]]
print(b[2][0]) 
print(a[2:5])
print(a[2:])
#print(a[8])  #error
#concatenation
c=[1,2,3] + [4,5,6]
print(c)

  