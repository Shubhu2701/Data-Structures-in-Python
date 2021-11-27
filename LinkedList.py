# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 13:22:12 2021

@author: shubh
"""

class Node:
    def __init__(self,data=None,nextNode=None):
        self.data=data
        self.nextNode=nextNode
        
class LinkedList:  
    def __init__(self):
        self.head=None
        
    def insertAtBegin(self,data):
        node=Node(data,self.head)
        self.head=node
        
    def insertAtEnd(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        
        itr=self.head
        while itr.nextNode:
            itr=itr.nextNode
            
        itr.nextNode=Node(data,None)
        
        
    def printList(self):
        if self.head is None:
            print("List is empty")
            return
        
        itr=self.head
        while itr:
            print(str(itr.data),end=" , ")
            itr=itr.nextNode
    
    def getLength(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.nextNode
        return count
    
    def removeAt(self,index):
        if index<0 or index>=self.getLength():
            raise Exception("Invalid out of bounds")
            
        if index==0:
            self.head =self.head.nextNode
            return
        
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                itr.nextNode=itr.nextNode.nextNode
                break
            itr=itr.nextNode
            count+=1
            
    def insertAt(self,index,data):
        if index<0 or index>=self.getLength():
            raise Exception("Index out of bounds")
        
        if index==0:
            self.insertAtBegin(data)
            return
        
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                node=Node(data,itr.nextNode)
                itr.nextNode=node
                break
            itr=itr.nextNode
            count+=1
            
    def insertList(self,lst):
        for data in lst:
            self.insertAtEnd(data)
        
        
            

ll=LinkedList()
ll.insertAtBegin(22)
ll.insertList([2,5,6,2,6,88,])
ll.insertAtBegin(520)
ll.insertAtEnd(69)
ll.removeAt(8)
ll.insertAt(4,69) 
ll.printList()
