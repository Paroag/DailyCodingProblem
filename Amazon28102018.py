#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 14:55:25 2019

@author: oscarbarbier

Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Given an integer k and a string s, find the length of the longest substring that 
    contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
"""

'''solution Oscar'''

s = "initation"
k = 4

# {index : [[letters_seen], LENGTH]}

def problem_solver(s, k) :
    dic = {}
    maxi = 0
    for index, letter in enumerate(list(s)) :
        print(dic)
        for key in list(dic) :
            if letter in dic[key][0] :
                dic[key][1] += 1
            else :
                if len(dic[key][0]) < k :
                    dic[key][0].append(letter)
                    dic[key][1] += 1
                else :
                    maxi = max(maxi, dic.pop(key)[1])
        dic[index] = [[letter], 1]
    return maxi # il manque un checkde l'état du dictionnaire

print(problem_solver(s, k))
