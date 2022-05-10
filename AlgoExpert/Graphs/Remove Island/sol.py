# Time = O(n) or O(wh)
# space = O(n) or (wh)
def removeIslands(matrix):
	for row in range(len(matrix)):
		for col in range(len(matrix[row])):
			# check if the cur row and col are border
			isRowBorder = row == 0 or row == len(matrix) - 1
			isColBorder = col == 0 or col == len(matrix[row]) - 1
			
			if not isRowBorder and not isColBorder:
				continue
				
			if matrix[row][col] != 1:
				continue
				
			# Am at border - so Change all border and its neighbour ones to two
			changeOneToTwo(row,col,matrix)
	
	# once all my border and neighbour ones are turned to two - change them
	for row in range(len(matrix)):
		for col in range(len(matrix[row])):
			if matrix[row][col] == 2:
				matrix[row][col] = 1
			else:
				matrix[row][col] = 0
	
	return matrix

def changeOneToTwo(row,col,matrix):
	stack = [(row,col)]
	
	while len(stack)>0:
		curRow , curCol = stack.pop()
		
		matrix[curRow][curCol] = 2
		
		neighbours = getNeighbour(curRow, curCol, matrix)
		
		for neighbour in neighbours:
			row,col = neighbour
			
			if matrix[row][col] != 1:
				continue
				
			stack.append(neighbour)
	print(matrix)
			
def getNeighbour(row, col, matrix):
	neighbours = []
	
	# check if I am not at borers
	if row - 1 >= 0: # up
		neighbours.append((row-1,col))
		
	if row + 1 < len(matrix): #down
		neighbours.append((row+1,col))
		
	if col - 1 >= 0: # left
		neighbours.append((row,col-1))
		
	if col + 1 < len(matrix[row]):
		neighbours.append((row,col+1))
		
	return neighbours