"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Dropbox.

Given the root to a binary search tree, find the second largest node in the tree.
"""

# Solution Oscar

class Tree :

	def __init__(self, value = 0, right = None, left = None):
		self.value = value
		self.left = left
		self.right = right

tree324 = Tree(3, left = Tree(2, left = None, right = Tree(4)), right = None)
tree423 = Tree(4, left = Tree(2, left = None, right = Tree(3)), right = None)
tree342 = Tree(3, left = Tree(4, left = None, right = Tree(2)), right = None)

"""
TreeXYZ

X -- 
| 
Y -- Z
|

"""

def problem_solver(tree) :

	def find_maxs(tree) :
		if tree is None :
			return [0,0]
		elif not tree.right and not tree.left :
			return [tree.value, 0]
		else :
			maxs_left = find_maxs(tree.left)
			maxs_right = find_maxs(tree.right)
			maxs =[tree.value]+maxs_left+maxs_right
			maxs.sort()
			return([maxs[-1], maxs[-2]])

	return(find_maxs(tree)[1])

print(problem_solver(tree324))
print(problem_solver(tree423))
print(problem_solver(tree342))