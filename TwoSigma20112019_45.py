"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Two Sigma.

Using a function rand5() that returns an integer from 1 to 5 (inclusive) with uniform probability, implement a function rand7() that returns an integer from 1 to 7 (inclusive).
"""

from random import randint

def rand5() :
	return randint(0,5)

def rand7() :
	rand_vec = [rand5() for _ in range(7)]
	return(sum(rand_vec)%7+1)



print(rand7())

# On vérfie comme de bons informaticiens que la solution est uniforme ;)

dic = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0}

for _ in range(1000*1000) :
	dic[rand7()] += 1

print(dic)
