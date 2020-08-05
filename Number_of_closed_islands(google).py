grid = [[1,1,1,1,1,1,1],
        [1,0,0,0,0,0,1],
        [1,0,1,1,1,0,1],
        [1,0,1,0,1,0,1],
        [1,0,1,1,1,0,1],
        [1,0,0,0,0,0,1],
        [1,1,1,1,1,1,1]]

rows = len(grid)
cols = len(grid[0])

closedIslands = 0
if rows == 0:
	print(closedIslands)
	exit(0)

def isclosed(grid,i,j,rows,cols):
	if grid[i][j] == -1 or grid[i][j] == 1:
		return True
	if i==0 or i==rows-1 or j==0 or j==cols-1:
		return False
	grid[i][j] = -1
	left = isclosed(grid,i-1,j,rows,cols)
	right = isclosed(grid,i+1,j,rows,cols)
	bottom = isclosed(grid,i,j+1,rows,cols)
	top = isclosed(grid,i,j-1,rows,cols)
	return left and right and bottom and top

for i in range(1,rows-1):
	for j in range(1,cols-1):
		if grid[i][j] == 0:
			if isclosed(grid,i,j,rows,cols):
				closedIslands+=1
print(closedIslands)

