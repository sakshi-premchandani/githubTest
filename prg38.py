# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 20:59:36 2023

@author: DELL
"""

class node():
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class tree():
    def __init__(self):
        self.root=None
    def insert(self,val):
        if self.root==None:
            newnode=node(val)
            self.root=newnode
        point=self.root
        while(point.left!=None):
            point=point.left
        point=point.root
        while(point.right!=None):
            point=point.right
            
c=tree()
c.insert(4)
c.insert(5)
c.insert(7)
print(c.root.val)
print(c.root.left.val) 