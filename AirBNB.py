#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 09:43:46 2019

@author: oscarbarbier

Good morning! Here's your coding interview problem for today.

This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of
 non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. 
[5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?

"""

Solution Oscar

def function(l) :
    def largest_sum(l, dic, key) :
        if key in dic :
            return (dic[key], dic, key)
        else :
            if len(l) == 1 :
                dic[key] = max(l)
                return(max(l), dic, key)
            if len(l) == 2 :
                dic[key] = max(l)
                return (max(l), dic, key)
            else :
                val1, dic, keyX = largest_sum(l[1:], dic, key-1)
                val2, dic, keyX = largest_sum(l[2:], dic, key-2)
                value = max (l[0] + val2, val1)
                dic[key] = value
                return(value, dic, key)
    dic = {}
    result = largest_sum(l, dic, 0)[0]
    return result 

