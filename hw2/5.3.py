# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 15:41:47 2014

@author: gregory
"""

def check_fermat(a,b,c,n):
    if a**n+b**n==c**n and n>2:
        print 'Holy smokes, Fermat was wrong!'
        
    else:
        print "No, that doesn't work"
        
check_fermat(1,2,3,2)