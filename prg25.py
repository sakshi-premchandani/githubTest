# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 21:27:58 2023

@author: DELL
""" 

class node():
    def __init__(self,val):
        self.val=val
        self.next=None
class stack():
    def __init__(self):
        self.head=None
    
    def insert(self,new):
        if self.head == None:
            self.head=node(new)
        else:
            newnode=node(new)
            newnode.next=self.head
            self.head=newnode
c=stack()
c.insert(4)
c.insert(5)