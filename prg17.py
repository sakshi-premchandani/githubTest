# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 18:58:49 2023

@author: DELL
"""
c1=0
strlist=["abc","ab","bc"]
query=["ab","bc","abc"]
for i in range(len(query)):
    for j in range(len(strlist)):
        if(query[i]==strlist[j]):
            c1=c1+1
    print(c1)
    c1=0
#print(b)        