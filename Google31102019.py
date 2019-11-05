"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Implement regular expression matching with the following special characters:

    . (period) which matches any single character
    * (asterisk) which matches zero or more of the preceding element

That is, implement a function that takes in a string and a valid regular expression and returns whether or not the string matches the regular expression.

For example, given the regular expression "ra." and the string "ray", your function should return true. The same regular expression on the string "raymond" should return false.

Given the regular expression ".*at" and the string "chat", your function should return true. The same regular expression on the string "chats" should return false.
"""

# Solution Oscar

def problem_solver(string, regex) :
	print(string, regex)
	if string == "" :
		if regex.replace("*", "") == "" :
			return True
		else :
			return False
	elif regex == "" and string != "" :
		return False
	elif string[0] == regex[0] :
		return problem_solver(string[1:], regex[1:])
	elif regex[0] == "." :
		return problem_solver(string[1:], regex[1:])
	elif regex[0] != "*" and string[0] != regex[0] :
		return False
	elif regex[0] == "*" :
		return(problem_solver(string[1:], regex) or problem_solver(string, regex[1:]))


print(problem_solver("chat", ".*at"))
print(problem_solver("chats", ".*at"))
print(problem_solver("chachachacha", "cha*cha"))
