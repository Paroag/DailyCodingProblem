#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 15:36:47 2019

@author: oscarbarbier
"""

import math

def parmi(k, n) :
    return int(math.factorial(n)/math.factorial(k)/math.factorial(n-k))
    
def probleme(N) :
    somme = 0
    l = []
    for nb_2 in range(int(N/2)+1) :
        somme += parmi(nb_2, N-nb_2)
        l = l + get_liste(nb_2, N-nb_2)
    return(l)
    
def get_liste(nb_2, N) :
    # retourne toutes les combinaisons de nb_2 2 dans une liste de longueur N
    if N == 1 :
        if nb_2 == 0 :
            return([[1]])
        elif nb_2 == 1 :
            return([[2]])
    elif N > 1 and nb_2 == 0 :
        smaller = get_liste(nb_2, N-1)
        result = [([1]+liste) for liste in smaller]
        return(result)
    elif N == nb_2 :
        smaller = get_liste(nb_2-1, N-1)
        result = [([2]+liste) for liste in smaller]
        return result
    elif N > 1 and nb_2 != 0 :
        smaller = get_liste(nb_2-1, N-1)
        result_2 = [([2]+liste) for liste in smaller]
        smaller = get_liste(nb_2, N-1)
        result_1 = [([1]+liste) for liste in smaller]    
        return(result_1+result_2)
             
print(probleme(4))