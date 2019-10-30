

This problem was asked by Google.

You are given an M by N matrix consisting of booleans that represents a board. 
    Each True boolean represents a wall. Each False boolean represents a tile you can walk on.

Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps 
    required to reach the end coordinate from the start. If there is no possible path, 
    then return null. You can move up, left, down, and right. You cannot move through walls. 
    You cannot wrap around the edges of the board.

For example, given the following board:

[[f, f, f, f],
[t, t, f, t],
[f, f, f, f],
[f, f, f, f]]


and start = (3, 0) (bottom left) and end = (0, 0) (top left), 
the minimum number of steps required to reach the end is 7, 
since we would need to go through (1, 2) because there is a wall 
everywhere else on the second row.
"""
Solution Oscar

m = [[False, False, False, False], [False, True, False, True], [False, False, False, False], [False, False, False, False]]
c1 = (3,0)
c2 = (0,0)

def problem_solver(c1, c2, m) :
    
    def get_neighboors(c, m) :
        (x,y) = c
        l = []
        if x-1 >= 0 and not m[x-1][y] :
            l.append((x-1, y))
        if y-1 >= 0 and not m[x][y-1] :
            l.append((x, y-1))
        if x+1 < len(m[0]) and not m[x+1][y] :
            l.append((x+1, y))
        if y+1 < len(m) and not m[x][y+1] :
            l.append((x, y+1))
        return(l)

    it = 0
    frontier = [c1]
    dic = {c1 : it} 
    
    while c2 not in dic :
        it += 1
        nfrontier = []
        for l in frontier :
            neighboors = get_neighboors(l, m)
            for neighboor in neighboors :
                if neighboor not in dic :
                    nfrontier.append(neighboor)
                    dic[neighboor] = it
                else :
                    pass
        frontier = nfrontier
    return(dic[c2])
        
print(problem_solver(c1, c2, m))
