#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 10:01:11 2019

@author: oscarbarbier

Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Suppose we represent our file system by a string in the following manner:

The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

dir
    subdir1
    subdir2
        file.ext
The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.

The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:

dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a 
    file file1.ext and an empty second-level sub-directory subsubdir1. subdir2 contains 
    a second-level sub-directory subsubdir2 containing a file file2.ext.

We are interested in finding the longest (number of characters) absolute path to a file 
    within our file system. For example, in the second example above, the longest absolute 
    path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 
    (not including the double quotes).

Given a string representing the file system in the above format, 
    return the length of the longest absolute path to a file in the abstracted file system. 
    If there is no file in the system, return 0.

Note:

The name of a file contains at least a period and an extension.

The name of a directory or sub-directory will not contain a period.
"""

class Pile():
    
    def __init__(self):
        self.dict = {}
        self.index = 0
        
    def add(self, val):
        self.dict[self.index] = val
        self.index += 1
    
    def pop(self):
        if self.index > 0 :
            self.index += -1
            return(self.dict.pop(self.index), None)
        else :
            pass
        
    def length(self):
        return(self.index)
        
    def sum(self):
        return(sum([self.dict[key] for key in self.dict]))
    

def problem_solver(string) :
    lines = string.split("\n")
    pile = Pile()
    dic = {}
    for index, line in enumerate(lines) :
        nb_tab = line.count("\t")
        if nb_tab > pile.length() :
            pile.add(len(lines[index-1].replace("\t","")))
        elif nb_tab < pile.length():
            while nb_tab < pile.length() :
                pile.pop()
        dic[line] = len(line.replace("\t", "")) + pile.sum() + pile.length()
    return(max([dic[key] for key in dic]))
        
print(problem_solver("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"))



