# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 11:51:02 2021

@author: shubh
"""

class HashMap:
    def __init__(self):
        self.Max=10
        self.arr=[[] for i in range(self.Max)]
        
    def getHash(self,key):
        h=0
        for i in key:
            h+=ord(i)
        return h%self.Max
    
    def __setitem__(self,key,value):
        h=self.getHash(key)
        found=False
        for idx, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0]==key:
                self.arr[h][idx]=(key,value)
                found=True
                break
        if not found:
            self.arr[h].append((key,value))
                
    def __getitem__(self,key):
        h=self.getHash(key) 
        for elem in self.arr[h]:
            if elem[0]==key:
                return elem[1] 
    
    def __delitem__(self,key):
        h=self.getHash(key)
        for idx,elem in enumerate(self.arr[h]):
            if elem[0]==key and len(elem)==2:
                del self.arr[h][idx]
    
h1=HashMap()
h1["march 6"]=420
h1["march 7"]=22
h1["jan 20"]=69
h1["jan 20"]=70
h1["march 17"]=22
print(h1["march 17"])
del h1["march 17"]
print(h1["march 17"])

#print(h1.arr)