#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 15:13:20 2019

@author: oscarbarbier

Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message,    
    count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""

def count_decode (chaine) :
    if len(chaine) == 1 or not chaine :
        return 1
    elif int(chaine[0]) > 2 :
        return(count_decode(chaine[1:]))
    elif chaine[0] == "2" :
        if int(chaine[1]) > 6 :
            return(count_decode(chaine[1:]))
        elif int(chaine[1]) == 0 :
            return(count_decode(chaine[2:]))
        else :
            return(count_decode(chaine[1:]) + count_decode(chaine[2:]))
    elif chaine[0] == "1" :
        if int(chaine[1]) == 0 :
            return(count_decode(chaine[2:]))
        else :
            return(count_decode(chaine[1:]) + count_decode(chaine[2:]))
            



