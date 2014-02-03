# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 15:46:13 2014

@author: gregory
"""

def compare(x,y):
    if x > y:
        return 1
    elif x== y:
        return 0
        
    else:
        return  -1
        
a=compare(1,3)
print a
