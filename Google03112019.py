# coding: utf8

"""
This problem was asked by Google.

The edit distance between two strings refers to the minimum number of character insertions, deletions, and substitutions required to change one string to the other. 
For example, the edit distance between “kitten” and “sitting” is three: substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

Given two strings, compute the edit distance between them.
"""

def distance_edit(string1, string2) :
	if len(string1) < len(string2) :
		return(distance_edit(string2, string1))
	elif string1 == string2 :
		return 0
	elif string1 == "" or string2 == "" :
		return(max(len(string1), len(string2)))
	elif string1[0] == string2[0] :
		return(distance_edit(string1[1:], string2[1:]))
	else :
		return(1 + min(
			distance_edit(string1[1:], string2), #on vire une lettre
			distance_edit(string1, string1[0]+string2), # on rajoute une lettre
			distance_edit(string1, string1[0] + string2[1:]) #on remplace une lettre
			))


print(distance_edit("sittng", "sitting"))