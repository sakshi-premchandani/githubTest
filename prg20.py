# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 20:52:40 2023

@author: DELL
"""

a="welcome to raipur"
b=a.split(' ')
print(b[0])
print(b[0][1])
c=a.split('e')
print(c)
vowel=0
cons=0
for i in range(len(a)):
    if a[i]=='a' or a[i]=='e' or a[i]=='i' or a[i]=='u' or a[i]=='o':
        vowel=vowel+1
    else:
        cons=cons+1
print(vowel)
print(cons)