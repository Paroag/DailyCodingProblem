#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 11:55:05 2019

@author: oscarbarbier
"""

"""
Given an array of integers, return a new array such that each element at index i of the
  new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. 
    If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""

'''Solution Oscar'''

def problem_solver_ez(liste) :
    c = 1
    for val in liste :
        c = c * val
    return([int(c/val) for val in liste])
    
def problem_solver_hard(liste) :
    base = [1] * len(liste)
    for index, val in enumerate(liste) :
        for index2, val2 in enumerate(base) :
            if index==index2 :
                pass
            else :
                base[index2] = base[index2]*val
    return base
    
print(problem_solver_hard([3, 2, 1]))
