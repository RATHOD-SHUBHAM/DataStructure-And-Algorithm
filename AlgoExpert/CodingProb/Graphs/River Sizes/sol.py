# Time = O(row_len * col_len)
# Space = O(row_len * col_len) # visited nodes

def riverSizes(matrix):
	row_len = len(matrix)
	col_len = len(matrix[0])

	# final result
	final_riverSize = []

	# keep track of visited node
	visited= [[False for _ in range(col_len) ] for _ in range(row_len) ]

	for i in range(row_len):
		for j in range(col_len):
			# if land
			if matrix[i][j] == 0:
				continue
				
			# if the cell is already visited
			if visited[i][j]:
				continue
		
			# if the cell is not visited and is a river
			# get the river size
			riverSize = traverseNode(i, j, matrix, visited)

			# if the river size is more than zero, add to op 
			if riverSize > 0:
				final_riverSize.append(riverSize)
			
	return final_riverSize

def traverseNode(i, j, matrix, visited):
	currentRiverSize = 0
	
	# Stack
	stack = [[i,j]] # node to be explored

	while stack:
		i, j = stack.pop()

		# if land
		if matrix[i][j] == 0:
			continue
			
		# if the cell is previously visited
		if visited[i][j] :
			continue
		
		# if not visited -- mark it as visited
		visited[i][j] = True

		# increase the cur size of the river
		currentRiverSize += 1
		
		# Explore the adjacent neighbor and return if it there is a river
		adjacentNeighbour = getAdjacentNeighbor(i,j,matrix,visited)
		
		for nei in adjacentNeighbour:
			stack.append(nei)

	return currentRiverSize
    
		

def getAdjacentNeighbor(i, j, matrix, visited):
	adj_nei = [] # get the adjacent neighbors, who  are not yet visited
	# looking at 4 direction and handling base case

	# look up 
	# if i is at start idx, ie 0, we dont have to look up
	if i > 0 and  visited[i-1][j] == False:
		adj_nei.append([i-1 , j])
		
	# look down
	# if i is at last row, we dont have to look down
	if i < len(matrix) - 1 and visited[i+1][j] == False:
		adj_nei.append([i+1,j])

	# look to the left
	# if we are at first col ie idx 0, we dont have to look left
	if j > 0 and visited[i][j-1] == False:
		adj_nei.append([i , j-1])
		
	# look right
	# if we are at last col, we dont have to look right
	if j < len(matrix[0]) - 1 and visited[i][j+1] == False:
		adj_nei.append([i , j+1])
		
	return adj_nei
