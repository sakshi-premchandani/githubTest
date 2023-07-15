# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 19:23:29 2023

@author: DELL
"""

h1=[1,2,1,1]
h2=[1,1,2]
h3=[1,1]
s1=sum(h1)
s2=sum(h2)
s3=sum(h3)
while h1 and h2 and h3:
    m=min(s1,s2,s3)
    while(s1>m):
        s1-=h1.pop(0)
    while(s2>m):
        s2-=h2.pop(0)
    while(s3>m):
        s3-=h3.pop(0)
    if s1==s2==s3:
        print(s1)
        break