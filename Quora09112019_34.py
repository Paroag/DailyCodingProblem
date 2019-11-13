"""

Good morning! Here's your coding interview problem for today.

This problem was asked by Quora.

Given a string, find the palindrome that can be made by inserting the fewest number of characters as possible anywhere in the word. If there is more than one palindrome of minimum length that can be made, return the lexicographically earliest one (the first one alphabetically).

For example, given the string "race", you should return "ecarace", since we can add three letters to it (which is the smallest amount to make a palindrome). There are seven other palindromes that can be made from "race" by adding three letters, but "ecarace" comes first alphabetically.

As another example, given the string "google", you should return "elgoogle".

"""

# Solution Oscar
# Not completed, I could not find any solution to this problem ...

def extract_common_char(string1, string2) :
	return(set(string1) & set(string2))

def reverse(string) :
	return(string[::-1])

def problem_solver(string) :

	if len(set(string)) == len(string) :
		return(string[::-1][:-1] + string)
	else :
		left_word = ""
		right_word = ""
		i = 0
		while not extract_common_char(left_word, right_word) :
			i += 1
			left_word = string[:i]
			right_word = string[len(string)-i:]
		common_letter = list(extract_common_char(left_word, right_word))[0]
		first_i = string.find(common_letter)
		last_i = len(string) - string[::-1].find(common_letter) - 1
		first_part = reverse(string[last_i+1:]) + string[:first_i+1]
		last_part = reverse(first_part)
		return(first_part+problem_solver(string[first_i+1:last_i])+last_part)


print(problem_solver("race")) #-> ecarace
print(problem_solver("google")) #-> elgoogle
print(problem_solver("iabcdba")) #-> iabdcdbai
print(problem_solver("ABCAXYZDCB")) #-> ???