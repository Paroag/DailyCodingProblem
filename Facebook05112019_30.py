"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

You are given an array of non-negative integers that represents a two-dimensional elevation map where each element is unit-width wall and the integer is the height. Suppose it will rain and all spots between two walls get filled up.

Compute how many units of water remain trapped on the map in O(N) time and O(1) space.

For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.

Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in the second, and 3 in the fourth index (we cannot hold 5 since it would run off to the left), so we can trap 8 units of water.
"""

# Solution Oscar

def problem_solver(relief) :
	top_water = [max(relief) for _ in relief]
	current_level = 0
	for i in range(len(relief)) :
		top_water[i] = max(current_level, relief[i])
		current_level = max(current_level, relief[i])
	current_level = 0
	for i in range(len(relief), 0, -1) :
		top_water[i-1] = min(top_water[i-1], max(current_level, relief[i-1]))
		current_level = max(current_level, relief[i-1])
	return(sum([top_water[i] - relief[i] for i in range(len(relief))]))

print(problem_solver([2, 1, 2]))
print(problem_solver([3, 0, 1, 3, 0, 5]))