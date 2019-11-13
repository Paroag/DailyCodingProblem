"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so that all the Rs come first, the Gs come second, and the Bs come last. 
You can only swap elements of the array.

Do this in linear time and in-place.

For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].
"""

# Solution Oscar
# Ce code est non bitable, mais je pense qu'il fait un tri de liste dans les conditions demandes
# A voir avec Charles
# Je ne le sortirai pas d'une sandbox par contre :p

def swap(l, i, j) :
	l[i], l[j] = l[j], l[i]
	return(l)

def problem_solver(liste) :
	bot = 0
	top = len(liste)-1
	g_bot = int(len(liste)/2)
	g_top = int(len(liste)/2)
	c = 0
	while bot <= g_bot or top >= g_top :
		reset = False
		while liste[bot] != "G" and bot < top:
			if liste[bot] == "R" :
				bot +=1
			elif liste[bot] == "B":
				while liste[top] == "B" :
					top -= 1
				liste = swap(liste, top, bot)
				top -= 1
				reset = True
		while liste[top] != "G" and bot < top:
			if liste[top] == "B" :
				top -= 1
			elif liste[top] == "R" :
				while liste[bot] == "R" :
					bot +=1 
				liste = swap(liste, top, bot)
				bot += 1
				reset = True
		if bot >= top :
			return(liste)
		if reset :
			continue
		left = int(g_top + g_bot) < int(top + bot)
		if c%2 == 0:
			if left :
				liste = swap(liste, bot, g_top)
				g_top += 1
			else :
				liste = swap(liste, bot, g_bot)
				g_bot -= 1
		else :
			if left :
				liste = swap(liste, top, g_top)
				g_top += 1
			else :
				liste = swap(liste, top, g_bot)
				g_bot -= 1
		c+=1

	return(liste)


print(problem_solver(['G', 'B', 'R', 'R', 'B', 'R', 'G']))
print(problem_solver(['G', 'G', 'G', 'R', 'B', 'R', 'G']))
print(problem_solver(['G', 'B', 'R', 'R', 'G', 'B', 'G']))
print(problem_solver(['B', 'R']))
print(problem_solver(['R', 'R', 'G', 'G', 'B', 'B']))
print(problem_solver(['R', 'R', 'R']))
print(problem_solver(['G', 'G']))


