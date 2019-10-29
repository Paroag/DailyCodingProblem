#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 16:30:12 2019

@author: oscarbarbier
"""

#X = [1.3, 2.3, 4.4]
X = [1.3, 2.3, 4.4]

def get_L1(X, Y) :
    diff = [abs(round(x - y, 5)) for (x, y) in zip(X, Y)]
    return(sum(diff))

def get_Y(X) :
    Y = [round(val) for val in X]
    diff = [round(x - y, 5) for (x, y) in zip(X, Y)]
    
    while round(sum(X)) != sum(Y) :
        if sum(Y) < round(sum(X)) :
            index = diff.index(max(diff))
            Y[index] += 1
            diff = [round(x - y, 5) for (x, y) in zip(X, Y)]
        elif sum(Y) < round(sum(X)) :
            index = diff.index(min(diff))
            Y[index] -= 1
            diff = [round(x - y, 5) for (x, y) in zip(X, Y)]
    return Y

print(get_L1(X, get_Y(X)))
print(get_Y(X))

