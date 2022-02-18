# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 23:30:09 2022

@author: shubh
"""

class BinarySearchTreeNode:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
    
    def addChild(self,data):
        if data==self.data:
            return
        if data < self.data:
            #if smaller than parent than add to left node
            if self.left:
                self.left.addChild(data)
            else:
                self.left=BinarySearchTreeNode(data)
        else:
            #else add to the right node
            if self.right:
                self.right.addChild(data)
            else:
                self.right=BinarySearchTreeNode(data)
    
    def inOrder(self):
        elements=[]
        if self.left:
            elements+=self.left.inOrder()           
        elements.append(self.data)       
        if self.right:
            elements+=self.right.inOrder() 
        return elements
    
    def preOrder(self):
        elements=[]
        elements.append(self.data)
        if self.left :
            elements+=self.left.preOrder()
        if self.right:
            elements+=self.right.preOrder()
        return elements
    
    def postOrder(self):
        elements=[]
        if self.left :
            elements+=self.left.postOrder()
        if self.right:
            elements+=self.right.postOrder()
        elements.append(self.data)
        return elements
    
    def search(self,val):
        if self.data==val:
            return True
        if val<self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val>self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
            
    def findMax(self):
        if self.right is None:
            return self.data
        return self.right.findMax()
    
    def findMin(self):
        if self.left is None:
            return self.data
        return self.left.findMin()
    
    def delete(self,val):
        if val<self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val>self.data:
            if self.right:
                self.right =self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
                
            minVal = self.right.findMin()
            self.data=minVal
            self.right=self.right.delete(minVal)
        return self
            
        
tree=BinarySearchTreeNode(4)
tree.addChild(17)
tree.addChild(4)
tree.addChild(1)
tree.addChild(20)
tree.addChild(9)
tree.addChild(23)
tree.addChild(18)
tree.addChild(34)


print(tree.preOrder())
print(tree.postOrder())
print(tree.inOrder())
tree.delete(4)
print(tree.inOrder())
print(tree.search(4))
