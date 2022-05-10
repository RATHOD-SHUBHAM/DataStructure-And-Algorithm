# checking each square size for a matrix
# Time = O(n^4)
# Space = O(1)
def squareOfZeroes(matrix):
	n = len(matrix)
	
	# min square size is 2. so go upto n-1
	for topRow in range(n-1):
		for leftCol in range(n-1):
			squareSize = 2
			while squareSize <= n - topRow and squareSize <= n - leftCol:
				bottomRow = topRow + squareSize - 1
				rightCol = leftCol + squareSize - 1
				
				if isSqaureBorder(matrix, topRow, leftCol, bottomRow, rightCol):
					return True
				
				# expand the size of square from a given point
				squareSize += 1
	return False

def isSqaureBorder(matrix, topRow, leftCol, bottomRow, rightCol):
	# Check if there are 0 in row
	for row in range(topRow, bottomRow + 1):
		if matrix[row][leftCol] != 0 or matrix[row][rightCol] != 0:
			return False
	
	# check if there are 0 in col
	for col in range(leftCol, rightCol + 1):
		if matrix[topRow][col] != 0 or matrix[bottomRow][col] != 0:
			return False
	
	return True