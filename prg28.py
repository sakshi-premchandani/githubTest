# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 19:32:59 2023

@author: DELL
"""

class node():
    def __init__(self,val):
        self.val=val
        self.next=None
class stack():
    def __init__(self):
        self.head=None
    def push(self,new):
        if self.head==None:
            newnode=node(new)
            self.head=newnode
        else:
            while(self.head.val>new):
                self.pop(sd)
            newnode=node(new)
            newnode.next=self.head
            self.head=newnode
            
    def pop(self,sd):    #sd is the new stack jisme push krna hai 
        sd.push(new)
        self.head=self.head.next
c=stack()
d=stack() 
c.push(5)
c.push(4)
c.pop(d)
      
        