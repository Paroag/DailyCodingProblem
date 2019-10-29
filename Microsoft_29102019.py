#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 13:47:37 2019

@author: oscarbarbier

Good morning! Here's your coding interview problem for today.

This problem was asked by Microsoft.

Given a dictionary of words and a string made up of those words (no spaces), 
return the original sentence in a list. If there is more than one possible reconstruction, 
return any of them. If there is no possible reconstruction, then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", 
you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string 
"bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].
"""

#Solution Oscar

def problem_solver(string, dic) : 
    
    def split_string(current, left, dic):
        """
           Return a Tuple (boolean, words)
           @ input  : current {string} a word or partially completed word
           @ input  : left {string} a concatenated list of words that still need to be processed
           @ input  : dic {list} a list with the vocabulary
           @ output : {(boolean, words)} The boolean tells wether or not it is possile to split current+left with the vocabulary
                                         The words gives a coherent split of current+left with the vocabulary
                                         
           Example :
               split_string("Hel", "loWorld", ["World", "Hello"]) returns (True, ["Hello", "World"])
               split_string("Sa", "lut", ["Hello", "World"]) returns (False, [])
       """           
        if left == "" :
            if current not in dic :
                return(False, [])
            else :
                return(True, [current])
        else :
            if current in dic and split_string("", left, dic)[0] :
                return(True, [current]+split_string("", left, dic)[1])
            else :
                return(split_string(current+left[0], left[1:], dic))
    
    return(split_string("", string, dic)[1])
    
    
# SAMPLE TEST (the last one is not provided but very important to ensure consistency)
print(problem_solver("thequickbrownfox",['the', 'quick', 'brown', 'fox']))
print(problem_solver("bedbathandbeyond", ['bed', 'bath', 'bedbath', 'and', 'beyond']))
print(problem_solver("HelloWorld", ["He", "Hello", "World"]))