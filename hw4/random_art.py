# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 11:34:57 2014

@author: pruvolo
"""

# you do not have to use these particular modules, but they may help
from random import randint
import Image
from math import pi,sin,cos,sqrt
import numpy as np
def build_random_function(min_depth, max_depth):
    #inputs a min and max depth and will output a nested list that contains strings of a random math equation
    flist=["prod","cos_pi","sin_pi",'divide2','square',"x","y"]
    if min_depth>0:     #checks if its ok to add an x or y to the random equation
        rand=randint(0,4) # if it does not acheive min x and y cant be added to the list
        if rand==0:
            return[flist[rand],build_random_function(min_depth-1,max_depth-1),build_random_function(min_depth-1,max_depth-1)]
        elif rand==1 or rand==2 or rand == 3 or rand== 4:
            return[flist[rand],build_random_function(min_depth-1,max_depth-1)]
    else:
        if max_depth==0: #if max depth is acheived x and y must be chosen
            rand=randint(5,6)
            return[flist[rand]]
        else:
            rand=randint(0,6)
            if rand==0:
                return[flist[rand],build_random_function(min_depth-1,max_depth-1),build_random_function(min_depth-1,max_depth-1)]
            elif rand==1 or rand==2 or rand== 3 or rand==4:
                return[flist[rand],build_random_function(min_depth-1,max_depth-1)]
            else:
                return[flist[rand]]
    # your code goes here
def evaluate_random_function(f, x, y):
    "inputs the build random function and x and y values and solves the random equation that is generated and outputs the answer"
    #all the if statements checks which function is used and solves the function
    if f[0] == 'prod':
        return evaluate_random_function(f[1],x,y)*evaluate_random_function(f[2],x,y)
    elif f[0] == 'cos_pi':
        return cos(evaluate_random_function(f[1],x,y)*pi)
    elif f[0] == 'sin_pi':
        return sin(evaluate_random_function(f[1],x,y)*pi)
    elif f[0] == 'x':
        return x
    elif f[0] == 'y':
        return y
    elif f[0] == "divide2":
        return (evaluate_random_function(f[1],x,y))/2
    elif f[0] =='square':
        return (evaluate_random_function(f[1],x,y))*(evaluate_random_function(f[1],x,y))
    # your code goes here
    
def colors(min_depth,max_depth):
    im = Image.new("RGB",(350,350)) # creates the map
    im2=im.load()
    #creates three random equations for each color
    Rf=build_random_function(min_depth, max_depth)
    Gf=build_random_function(min_depth, max_depth)
    Bf=build_random_function(min_depth, max_depth)
    #divides n into 350 numbers between -1 and 1. Each represents a pixel on the map
    n=np.linspace(-1,1,350)
    xp=0
    yp=0
    #finds the color for each pixel on the map
    for xp in range(len(n)):
        for yp in range(len(n)):
            red=evaluate_random_function(Rf, n[xp],n[yp])
            green=evaluate_random_function(Gf, n[xp],n[yp])
            blue=evaluate_random_function(Bf, n[xp],n[yp])
            #scales the color values to 250            
            red=int((red+1)*250/2)
            green=int((green+1)*250/2)
            blue=int((blue+1)*250/2)
            #combines the three colors for each pixel
            im2[xp,yp]=(red,green,blue)
    im.save("test2.bmp")
colors(5,7)
def remap_interval(val, input_interval_start, input_interval_end, output_interval_start, output_interval_end):
    
    """ Maps the input value that is in the interval [input_interval_start, input_interval_end]
        to the output interval [output_interval_start, output_interval_end].  The mapping
        is an affine one (i.e. output = input*c + b).
    
        TODO: please fill out the rest of this docstring
    """
    # your code goes here
    