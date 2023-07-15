# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 20:49:06 2023

@author: DELL
"""

mini=2
h1=[3,2,1,1]
s1=sum(h1)
while(s1>mini):
    s1-=h1.pop(0)
print(s1)