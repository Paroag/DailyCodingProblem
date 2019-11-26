"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given a array of numbers representing the stock prices of a company in chronological order, write a function that calculates the maximum profit you could have made from buying and selling that stock once. You must buy before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 5 dollars and sell it at 10 dollars.
"""

# Naive solution (0(n**2))

def problem_solver(liste) :
	rLis = liste[::-1]
	profit = 0
	for index, val1 in enumerate(rLis) :
		for val2 in rLis[index+1:] :
			profit = max(profit, val1 - val2)
	return profit

print(problem_solver([9, 11, 8, 5, 7, 10]))