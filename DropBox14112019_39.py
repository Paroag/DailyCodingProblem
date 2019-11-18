"""Good morning! Here's your coding interview problem for today.

This problem was asked by Dropbox.

Conway's Game of Life takes place on an infinite two-dimensional board of square cells. Each cell is either dead or alive, and at each tick, the following rules apply:

    Any live cell with less than two live neighbours dies.
    Any live cell with two or three live neighbours remains living.
    Any live cell with more than three live neighbours dies.
    Any dead cell with exactly three live neighbours becomes a live cell.

A cell neighbours another cell if it is horizontally, vertically, or diagonally adjacent.

Implement Conway's Game of Life. It should be able to be initialized with a starting list of live cell coordinates and the number of steps it should run for. Once initialized, it should print out the board state at each step. Since it's an infinite board, print out only the relevant coordinates, i.e. from the top-leftmost live cell to bottom-rightmost live cell.

You can represent a live cell with an asterisk (*) and a dead cell with a dot (.)."""

import numpy as np
import time
from PIL import Image

class LifeBoard :

	def __init__(self, array) :
		self.array = array

	def counts_neighboors(self, i, j) :
		c = 0
		for delta_x in [-1, 0, 1] :
			for delta_y in [-1, 0, 1] :
				if (delta_x, delta_y) != (0,0) and i+delta_x >= 0 and j+delta_y >= 0:
					try :
						c += self.array[i+delta_x, j+delta_y]
					except IndexError :
						pass
		return c

	def truncate(self) :
		if self.array.shape == (0,0) :
			return False
		for x in range(self.array.shape[0]) :
			if self.array[x, 0] == 1 or self.array[x, -1] == 1 :
				return False
		for y in range(self.array.shape[1]) :
			if self.array[0, y] == 1 or self.array[-1, y] == 1:
				return False
		self.array = self.array[1:-1, 1:-1]
		return True


	def iterate(self) :
		extended_array = np.zeros([self.array.shape[0]+2, self.array.shape[1]+2])
		extended_array[1:-1, 1:-1] = self.array
		self.array = extended_array

		new_arr = np.zeros([self.array.shape[0], self.array.shape[1]])

		for x in range(new_arr.shape[0]) :
			for y in range(new_arr.shape[1]) :
				neighboors = self.counts_neighboors(x, y)
				if self.array[x, y] == 1 :
					if neighboors < 2 or neighboors > 3 :
						new_arr[x, y] = 0
				else :
					if neighboors == 3 :
						new_arr[x, y] = 1

		self.array = new_arr
		while(self.truncate()) :
			pass
		return True

	def process(self, iter = 10, timer = 1) :
		print(self.array)
		for _ in range(iter) :
			print("----------")
			self.iterate()
			time.sleep(timer)
			print(self.array)
			img = Image.fromarray(self.array, mode = '1')
			img.show()

	def __str__(self) :
		return(self.array)

if __name__ == "__main__" :

	arr = np.random.randint(5, size = (2056, 2056))
	for x in range(arr.shape[0]) :
		for y in range(arr.shape[1]) :
			arr[x][y] = min(arr[x][y], 1)
	lf = LifeBoard(arr)
	lf.process(iter = 3)

