"""

Good morning! Here's your coding interview problem for today.

This problem was asked by Quora.

Given a string, find the palindrome that can be made by inserting the fewest number of characters as possible anywhere in the word. If there is more than one palindrome of minimum length that can be made, return the lexicographically earliest one (the first one alphabetically).

For example, given the string "race", you should return "ecarace", since we can add three letters to it (which is the smallest amount to make a palindrome). There are seven other palindromes that can be made from "race" by adding three letters, but "ecarace" comes first alphabetically.

As another example, given the string "google", you should return "elgoogle".

"""

# Solution Oscar
# Not completed, I could not find any solution to this problem ...

def problem_solver(string) :

	def is_palindrome(s) :
		if len(s) < 2 :
			return True
		else :
			return(s[0]==s[-1] and is_palindrome(s[1:-1]))



	

print(problem_solver("race")) #-> ecarace
print(problem_solver("google")) #-> elgoogle
print(problem_solver("iabcdba")) #-> iabdcdbai