# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 01:22:23 2021

@author: shubh
"""

class Node:
    def __init__(self,data=None,nextNode=None,preNode=None):
        self.data= data
        self.nextNode=nextNode
        self.preNode=preNode
        
class DoublyLinkedList:
    def __init__(self):
        self.head=None
        
    def insertAtBegin(self,data):
        node=Node(data,self.head,None)
        self.head=node
        
    def insertAtEnd(self,data):
        if self.head is None:
            self.head=Node(data,None,None)
        
        itr=self.head
        while itr.nextNode:
            itr=itr.nextNode
        itr.nextNode=Node(data,None,itr)
    
    def insertList(self,lst):
        for data in lst:
            self.insertAtEnd(data)
    
    def getLength(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.nextNode
        return count
    
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
                node=Node(data,itr.nextNode,itr)
                itr.nextNode.preNode=node
                itr.nextNode=node
                break
            itr=itr.nextNode
            count+=1
            
    def printList(self):
        if self.head is None:
            print("List is empty")
            return
        
        itr=self.head
        while itr:
            print(str(itr.data),end=" , ")
            itr=itr.nextNode
            
    def removeAt(self,index):
        if index<0 or index>=self.getLength():
            raise Exception("Index out of bounds")
            
        if index==0:
            self.head.nextNode.preNode=None
            self.head=self.head.nextNode 
            return
                    
        count=0
        itr=self.head              
        length=self.getLength()
        while itr:
            if count==index-1 and index==length-1:
                itr.nextNode.preNode=None
                itr.nextNode=None
                break
        
            if count==index-1:
                itr.nextNode.nextNode.preNode=itr
                itr.nextNode=itr.nextNode.nextNode
                break
            itr=itr.nextNode
            count+=1
            
                     

ll=DoublyLinkedList()
ll.insertAtBegin(22)
ll.insertList([2,5,6,2,6,88])
ll.insertAtEnd(69)
ll.removeAt(7)
ll.insertAt(4,3) 
ll.printList()
            