"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
"""

# Solution Oscar

def problem_solver(string) : 
	dic = {"(" : ")", "{" : "}", "[" : "]"}
	state = []
	for char in string :
		if char not in dic :
			if dic[state.pop()] != char :
				return False
		else :
			state.append(char)
	if state :
		return False
	else :
		return True


print(problem_solver("(({}))"))
print(problem_solver("{}[]"))
print(problem_solver("(({}"))
print(problem_solver("(({]))"))

