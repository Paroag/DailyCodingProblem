"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Microsoft.

Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of the list so far on each new element.

Recall that the median of an even-numbered list is the average of the two middle numbers.

For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:

2
1.5
2
3.5
2
2
2
"""

# Solution Oscar
# problably non optimized, n**2 complexity

def problem_solver(liste) :

	#defining median funtion
	def median(l) :
		l.sort()
		if len(l)%2 == 1 :
			return(l[int((len(l)-1)/2)])
		else :
			return( (l[int(len(l)/2)-1]+l[int(len(l)/2)])/2 )

	return([float(median(liste[:i+1])) for i, val in enumerate(liste)])

print(problem_solver([2, 1, 5, 7, 2, 0, 5]))