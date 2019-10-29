#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 10:05:56 2019

@author: oscarbarbier

Given an array of integers, find the first missing positive integer in linear time 
    and constant space. In other words, find the lowest positive integer that does 
    not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.

"""
Solution Charles

def solution_with_set(l):
    s, res = set(l), 0
    while res in s:
        res += 1
    return res

def solution_with_dic(l):
    n = len(l)
    d = {x: False for x in range(n)}
    res = 0
    for val in l:
        if (0 <= val) and (val < n):
            d[val] = True
        if val == res:
            while res < n and d[res]:
                res += 1
    return res




Solution Oscar

import bisect #insert elements to sorted list

l = [3, 4, -1, 0]

def get_first_missing_integer(l) :
    seen = []
    c = 0
    for val in l :      
        if val == c+1 :
            c = val
        elif val <= c :
            continue
        else :
            bisect.insort(seen,val)
        
        while seen and seen[0] == c+1 :
            c += 1
            del seen[0]
            
    return c+1

print(get_first_missing_integer(l))

#    seen.insort(l, 3)
