# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 14:46:15 2023

@author: DELL
"""

st1=[]
st2=[]
class qu():
    def insert(self,new):
        st1.append(new)
    def out(self):
        while len(st1)!=0:
            t=st1.pop()
            st2.append(t)
        st2.pop()
        while len(st2)!=0:
            k=st2.pop()
            st1.append(k)
p=qu()
p.insert(9)
p.insert(8)
p.out()
print(st1)