"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.

For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

You may also use a list or array to represent a set.
"""

# Solution Oscar
# Doing it with list (we do not mind about order)

def problem_solver(liste) :

	def pick(l, nb_elem) :
		# all comination of nb_elem elem of list l
		# input : l <list>, nb_elem <int>
		# output : <list> of <list>
		if nb_elem == 0 :
			return [[]]
		else :
			if nb_elem == len(l) :
				return [l]
			else :
				return( pick(l[1:], nb_elem) + [[l[0]]+ val for val in pick(l[1:], nb_elem-1)] )

	power_list = []
	for nb_elem in range(len(liste)+1) :
		power_list += pick(liste, nb_elem)

	return power_list

print(problem_solver([1, 2, 3, 4]))