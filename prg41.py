# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 19:27:25 2023

@author: DELL
"""

#append strin w to string s
stack=[]
s="sjdbkb" 
w="sakshi"
s=s+w 
stack.append(s)
#removing k characters
x=list(map(str,w))
k=4
while(k>0):
    if x:
       x.pop()
    k=k-1
print(x)
#print kth character of x
k=2
print(x[k-1])
    