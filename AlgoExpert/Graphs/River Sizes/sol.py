# Time = O(n)
# Space = O(n)

def riverSizes(matrix):
	# final result
	size = []
	# keep track of visited node
	visited= [[False for _ in row ] for row in matrix ]
	
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			# check if they are visitied
			if visited[i][j]:
				continue
		
			traverseNode(i,j,matrix,visited,size)
			
	return size

def traverseNode(i,j,matrix,visited,size):
	currentRiverSize = 0
	
	# Stack
	stack = [[i,j]]
	
	while len(stack):
		i, j = stack.pop()
		
		if visited[i][j] :
			continue
		
		# if not visited -- mark it as visited
		visited[i][j] = True
		
		# if land
		if matrix[i][j] == 0:
			continue
		
		currentRiverSize += 1
		
		exploreNeighbour = explore(i,j,matrix,visited)
		
		for nodes in exploreNeighbour:
			stack.append(nodes)
	
	if currentRiverSize > 0:
		size.append(currentRiverSize)
		

def explore(i,j,matrix,visited):
	unvisited = []
	
	# looking at 4 direction and handling base case
	if i > 0 and  visited[i-1][j] == False:
		unvisited.append([i-1 , j])
		
	if i < len(matrix) - 1 and visited[i+1][j] == False:
		unvisited.append([i+1,j])
	
	if j > 0 and visited[i][j-1] == False:
		unvisited.append([i , j-1])
		
	if j < len(matrix[0]) - 1 and visited[i][j+1] == False:
		unvisited.append([i , j+1])
		
	return unvisited