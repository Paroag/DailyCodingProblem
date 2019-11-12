"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Jane Street.

Suppose you are given a table of currency exchange rates, represented as a 2D array. Determine whether there is a possible arbitrage: 
that is, whether there is some sequence of trades you can make, starting with some amount A of any currency, so that you can end up with 
some amount greater than A of that currency.

There are no transaction costs and you can trade fractional quantities.
"""

"""

NO ARBITRAGE :

		DOLLAR	 EURO  YUN
DOLLAR     1	 2     10 
EURO       0.5   1     5
YUN        0.1   0.2   1

ARBITRAGE :

		DOLLAR	 EURO  YUN
DOLLAR     1	 1     10 
EURO       1     1     5
YUN        0.1   0.2   1

"""

no_arbitrage = [[1, 2, 10], [0.5, 1, 5], [0.1, 0.2, 1]]
arbitrage = [[1, 1, 10], [1, 1, 5], [0.1, 0.2, 1]]

def problem_solver(liste):
	reference = liste[0]
	for other_money in liste[1:] : #liste au moins de longueur 2 sinon pas de sens
		other_money_scaled = [val/other_money[0] for val in other_money]
		if other_money_scaled != reference :
			return(True)
	return(False)

print(problem_solver(arbitrage))
print(problem_solver(no_arbitrage))
