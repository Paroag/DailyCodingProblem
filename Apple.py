#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 17:07:40 2019

@author: oscarbarbier

Good morning! Here's your coding interview problem for today.

This problem was asked by Apple.

Implement a job scheduler which takes in a function f and an integer n, 
    and calls f after n milliseconds.

Upgrade to premium and get in-depth solutions to every problem, including this one.

If you liked this problem, feel free to forward it along so they 
    can subscribe here! As always, shoot us an email if there's anything we can help with!

Ready to interview? Take Triplebyte's quiz and skip straight 
    to final interviews with top tech companies!
"""

import time

def f_retard(f, n, **args):
    time.sleep(n/1000)
    return(f(**args))
    
def print_1(string = "Hello World"):
    print(string)

f = print_1

f_retard(print_1, 2000, string = "Coucou")
