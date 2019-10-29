#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 12:38:58 2019

@author: oscarbarbier
"""

"""
A typical American-style crossword puzzle grid is an N x N matrix with black and white squares, which obeys the following rules:

    1
    Every white square must be part of an "across" word and a "down" word.
    No word can be fewer than three letters long.
    
    2
    Every white square must be reachable from every other white square.
    
    3
    The grid is rotationally symmetric (for example, the colors of the top left and bottom right squares must match).

Write a program to determine whether a given matrix qualifies as a crossword grid.

We will be sending the solution tomorrow, along with tomorrow's question. As always, feel free to shoot us an email if there's anything we can help with.

Have a great day!
"""

import numpy as np

  
C = np.ones(shape = (3, 3), dtype =  np.int8)
I = np.random.randint(2, size=(3, 3))
T = np.array([[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])

# get the first 0 of a 0 sequence (based on index)
def get_length_word(index, word) :
    if word[index] == 1 :
        return 0
    elif index == len(word)-1 or index == 0:
        return 1   
    else :
        return get_length_word(index-1, word) + get_length_word(index-1, word)
    
print(get_length_word(0 , [0,0,1,1,1,0,0,0,0,1,0,0]))
    

def check_condition_1(array) :
    for row in array :
        for letter in row :
            if row[letter] == 0 :
                if get_word_length(get_first_0(letter, row), row) < 3 :
                    return False
    for row in array.transpose() :
        for letter in row :
            if row[letter] == 0 :
                if get_word_length(get_first_0(letter, row), row) < 3 :
                    return False
    return True

print(check_condition_1(T))
    

def check_condition_2(array) :
    return False
    
def check_condition_3(array) :
    return False

def is_crossword_grid(array) :
    return check_condition_1(array) and check_condition_2(array) and check_condition_3(array)
