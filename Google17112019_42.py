"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k. If such a subset cannot be made, then return null.

Integers can appear more than once in the list. You may assume all numbers in the list are positive.

For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24.
"""

def problem_solver(liste, k) :

	liste.sort()

	def find_subset(subset, liste, k) :
		if sum(subset) > k :
			return False, []
		elif sum(subset) == k :
			return True, subset
		else :
			if not liste :
				return False, []
			else :
				if find_subset(subset+[liste[0]], liste[1:], k)[0] :
					return(find_subset(subset+[liste[0]], liste[1:], k))
				elif find_subset(subset, liste[1:], k)[0] :
					return(find_subset(subset, liste[1:], k))
				else :
					return(False, [])

	return(find_subset([], liste, k)[1])

print(problem_solver([12, 1, 61, 5, 9, 2], 24))