# Time  = O(n) or O(wh)
# space = O(n) or (wh)

#eg: at first pass -- all the neighbours of positive element should turn positive
def minimumPassesOfMatrix(matrix):
	passes = countPasses(matrix)
	# in the finall pass ill have no more elements to convert but ill still have value in queue which will increase the pass number by 1
	return passes -1 if negativeMatrix(matrix) else -1

# check if any cell cant be changed to positive
def negativeMatrix(matrix):
	for row in range(len(matrix)):
		for col in range(len(matrix[row])):
			if matrix[row][col] < 0:
				return False
	return True

def countPasses(matrix):
	# count the no of poitive cell in each pass and add it to queue
	queue = positiveMatrix(matrix)
	
	passes = 0
	
	while len(queue) > 0:
		print("q - ",queue)
		curQueueLen = len(queue) # act as a counter
		
		while curQueueLen > 0:
			row , col = queue.pop(0)
			
			neighbours = getNeighbour(row,col,matrix)
			
			# check if there is a negative value - convert it to positive and add to queue
			for neighbor in neighbours:
				curRow, curCol = neighbor
				
				if matrix[curRow][curCol] < 0:
					matrix[curRow][curCol] *= -1
					queue.append(neighbor)
				
			curQueueLen -= 1
		
		passes += 1
		print("passes: ",passes)
		
	return passes

def positiveMatrix(matrix):
	positiveCell = []
	
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if matrix[i][j] > 0:
				positiveCell.append([i,j])
				
	return positiveCell

def getNeighbour(row,col,matrix):
	neighbours = []
	
	if row > 0:
		neighbours.append([row-1,col])
	if row < len(matrix) - 1:
		neighbours.append([row + 1,col])
	if col < len(matrix[row]) - 1:
		neighbours.append([row,col+1])
	if col > 0:
		neighbours.append([row,col-1])
	
	return neighbours