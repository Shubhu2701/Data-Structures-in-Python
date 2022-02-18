# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 13:57:22 2021

@author: shubh
"""

class Node:   
    def __init__(self, data):
        self.left=None
        self.right=None
        self.data=data
        
def createTree():
    print("Enter data")
    value=int(input())
    
    if value is -1:
        return
    
    root=Node(value)
    print("Enter data for the left node of "+str(root.data))
    root.left = createTree()
    print("Enter data for the right node of "+str(root.data))
    root.left = createTree()
    
    return root

def inOrder(root):
    if(root is None): return
    
    inOrder(root.left)
    print(root.data+" ")
    inOrder(root.right)
    
createTree()
