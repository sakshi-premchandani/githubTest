# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 20:49:38 2023

@author: DELL
"""

class node():
    def __init__(self,val):
        self.val=val
        self.prev=None
for i in range(10):
    a=node(i)
    a.prev=a
    print(a.val)
