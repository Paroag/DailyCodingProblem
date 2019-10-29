#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 16:30:42 2019

@author: oscarbarbier

Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 6 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \   \
 1   1   0

"""

class Arbre() :
    def __init__(self, value, left = None, right = None) :
        self.value = value
        self.left = left
        self.right = right

def is_unival(Arbre) :
    if Arbre.left == None and Arbre.right == None :
        return True, Arbre.value
    if Arbre.left == None :
        return ((is_unival(Arbre.right)[0] and Arbre.value == is_unival(Arbre.right)[1]), Arbre.value)
    if Arbre.right == None :
        return ((is_unival(Arbre.left)[0] and Arbre.value == is_unival(Arbre.left)[1]), Arbre.value)
    else :
        return ((is_unival(Arbre.left)[0] and is_unival(Arbre.right)[0] and Arbre.value == is_unival(Arbre.left)[1] and Arbre.value == is_unival(Arbre.right)[1]), Arbre.value)
    
def is_u(Arbre) :
    return is_unival(Arbre)[0]

def get_unival(Arbre) :
    if Arbre == None :
        return 0
    if Arbre.left == None and Arbre.right == None :
        return 1
    else :
        return(int(is_u(Arbre)) + get_unival(Arbre.left) + get_unival(Arbre.right))
    
if __name__ == "__main__" :
    
    Tree = Arbre(0, left=Arbre(1), right=Arbre(0, left = Arbre(1, left = Arbre(1), right = Arbre(1)),right = Arbre(0, right = Arbre(0))))
    unival = Arbre( 1, left = Arbre(1), right = Arbre(0) )
    
    print(get_unival(Tree))
