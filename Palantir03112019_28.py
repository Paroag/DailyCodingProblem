"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Palantir.

Write an algorithm to justify text. Given a sequence of words and an integer line length k, return a list of strings which represents each line, fully justified.

More specifically, you should have as many words as possible in each line. There should be at least one space between each word. Pad extra spaces when necessary so that each line has exactly length k. Spaces should be distributed as equally as possible, with the extra spaces, if any, distributed starting from the left.

If you can only fit one word on a line, then you should pad the right-hand side with spaces.

Each word is guaranteed not to be longer than k.

For example, given the list of words ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"] and k = 16, you should return the following:

["the  quick brown", # 1 extra space on the left
"fox  jumps  over", # 2 extra spaces distributed evenly
"the   lazy   dog"] # 4 extra spaces distributed evenly
"""

# Solution Oscat

def problem_solver(string, k):
	words = string.split()
	l = []
	l_string = []
	while words :
		wl = []
		while words and len(wl) + len(words[0]) + sum([len(w) for w in wl]) <= k :
			wl.append(words.pop(0))
		l.append(wl)
	for line in l :
		nb_white = k - sum([len(word) for word in line])
		line_string = ""
		for index, word in enumerate(line[:-1]) :
			line_string += word + (" "*(nb_white//(len(line)-1)))
			if index < (nb_white)%(len(line)-1) :
				line_string+=" " 
		line_string += line[-1]
		l_string.append(line_string)
	return l_string


print(problem_solver("the quick brown fox jumps over the lazy dog", 10))
