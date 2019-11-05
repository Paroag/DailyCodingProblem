"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given a singly linked list and an integer k, remove the kth last element from the list. k is guaranteed to be smaller than the length of the list.

The list is very long, so making more than one pass is prohibitively expensive.

Do this in constant space and in one pass.
"""

# Solution Oscar

def problem_solver(l, k) :
	i = 0
	new_l = []
	while len(l) > 0 :
		if i == k :
			i+=1 
			l.pop(0)
		else :
			i+=1 
			new_l.append(l.pop(0))
	return new_l

print(problem_solver([1,2,3], 1))

