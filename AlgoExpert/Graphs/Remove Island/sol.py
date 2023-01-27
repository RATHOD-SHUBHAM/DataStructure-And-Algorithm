# Time = O(n) or O(wh)
# space = O(n) or (wh)

'''
2 step process:
1. Mark all the island connected to bounday 
    * mark by converting all the boundary island to a random number
    for eg: say 2

2. once all the island that are connect to boundary are marked
    * Convert those island that are not marked to water
    ie convert all the island that are not converted to 2 - to )
    * Convert back the marked island to original number

'''

def removeIslands(matrix):
	row_len = len(matrix)
	col_len = len(matrix[0])

	visited = [[False for _ in range(col_len)] for _ in range(row_len)]

	# step 1: Mark all the island connected to bounday
	for row in range(row_len):
		for col in range(col_len):

			if visited[row][col]:
				continue
			
			# check if the cur row and col are border
			isRowBorder = row == 0 or row == len(matrix) - 1
			isColBorder = col == 0 or col == len(matrix[0]) - 1

			isBorder = isRowBorder or isColBorder

			# if it is not bounday - do nothing
			if not isBorder:
				continue
				
			# if it is not an island , do nothing
			if matrix[row][col] != 1:
				continue
				
			# We are at border that has a island  
			# Mark the island and all its adjacent island
			markIsland(row, col, matrix, visited)
	
    # print(matrix)

    # step 2: convert back all the marked island 
	for row in range(row_len):
		for col in range(col_len):
            # if the island is marked - convert back to orinal form
			if matrix[row][col] == 2:
				matrix[row][col] = 1
			else:
                # convert everything to water
                # if lsland is not marked - convert it to water
				matrix[row][col] = 0
	
	return matrix

def markIsland(row, col, matrix, visited):
	stack = [(row,col)]
	
	while stack:
		curRow , curCol = stack.pop()

		if visited[curRow][curCol]:
			continue

		if matrix[curRow][curCol] != 1:
			continue
		
		matrix[curRow][curCol] = 2
		visited[curRow][curCol] = True
		
		adj_neighbours = getNeighbour(curRow, curCol, matrix)
		
		for nei in adj_neighbours:	
			stack.append(nei)
            
	# print(matrix)
			
def getNeighbour(row, col, matrix):
	neighbours = []
	
	# check if I am not at borers
	if row > 0 and visited[row - 1][col] == False: # up
		neighbours.append((row - 1 ,col))
		
	if row < len(matrix) - 1 and visited[row + 1][col] == False: #down
		neighbours.append((row + 1,col))
		
	if col > 0 and visited[row][col - 1] == False: # left
		neighbours.append((row , col - 1))
		
	if col < len(matrix[0]) - 1 and visited[row][col + 1] == False:
		neighbours.append((row , col + 1))
		
	return neighbours
		