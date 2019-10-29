#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 13:10:38 2019

@author: oscarbarbier
"""

def problem_solver_naif(l, k) :
    for val1 in l :
        for val2 in l :
            if val1 + val2 == k :
                return True
    return False

def problem_solver(l, k) :
    d = {}
    for val in l :
        if val <= k :
            if k-val in d :
                return True
            else :
                d[val] = 0
    return False

if __name__ == "__main__" :
    
    l = [10, 15, 3, 7]
    k = 16
    
    print(problem_solver(l, k))


