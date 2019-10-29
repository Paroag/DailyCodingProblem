#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 15:51:59 2019

@author: oscarbarbier

Implement a queue using a set of fixed-length arrays.

The queue should support enqueue, dequeue, and get_size operations.
"""

l = [1, 4, 3, 5, 3, 2]

maxi = 0
for i in range(len(l)) :
    for j in range(l[i]) :
        k = i
        while k+1<len(l) and l[k+1] > j :
            k += 1
        e = k - i + 1
        print(i, j, e, e*(j+1))
        if e * (j+1) > maxi:
            maxi = e * (j+1)