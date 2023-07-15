# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 16:10:00 2023

@author: DELL
"""
b=[]
a=[[-9,-9,-9,1,1,1],[0,-9,0,4,3,2],[-9,-9,-9,1,2,3],[0,0,8,6,6,0],[0,0,0,-2,0,0],[0,0,1,2,4,0]]
#a=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
for i in range(len(a)-2):
    for j in range(len(a)-2):
        c=sum(a[i][j:j+3]+[a[i+1][j+1]])
        c1=c+sum(a[i+2][j:j+3])
        b.append(c1)
print(max(b))
        
    
        
#a[0][0:2]+a[1][1]+a[2][0:2]
#a[0][1:3]+a[1][2]+a[2][1:3]
#a[1][0:2]+a[2][1]+a[3][0:2]
#a[1][1:3]+a[2][2]+a[3][1:3]
        
       # c=sum(a[i][j:j+2],a[i+1][j+1])
       # c1=sum(c,a[i+2][j:j+2])
       # print(c1)
        #for k in range(2):
        #    suma=suma+a[i][k]+a[i+2][k]
       # suma=suma+a[i+1][j+1]
    