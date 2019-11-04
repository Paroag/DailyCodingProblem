#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 15:25:25 2019

@author: oscarbarbier

Good morning! Here's your coding interview problem for today.

This problem was asked by Twitter.

You run an e-commerce website and want to record the last N order ids in a log. 
Implement a data structure to accomplish this, with the following API:

record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
You should be as efficient with time and space as possible.

"""

'''solution Oscar'''

class fifo() :
    
    def __init__(self):
        self.index = 0
        self.fifo = {}
        
    def record(self, order_id):
        self.fifo[self.index] = order_id
        self.fifo.pop(self.index-1000, None)
        self.index += 1
        
    def get_last(self, i):
        return(self.fifo[self.index-i])
    
if __name__ == "__main__" :    
    tmp = fifo()
    for i in range(2000) :
        tmp.record(i)
    print(tmp.get_last(1000))
