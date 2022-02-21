# Time = O(n^3)
# space = O(n^2)

def squareOfZeroes(matrix):
    zeroCount = countZero(matrix)
	# print(zeroCount)
	
	n = len(matrix)
	for topRow in range(n-1):
		for leftCol in range(n-1):
			squareSize = 2
			
			while squareSize <= n - topRow and squareSize <= n - leftCol:
				bottomRow = topRow + squareSize - 1
				rightCol = leftCol + squareSize - 1
				
				if isSqaureBorder(zeroCount, squareSize, topRow, leftCol, bottomRow, rightCol):
					return True
				
				# expand the size of square from a given point
				squareSize += 1
	return False


def isSqaureBorder(zeroCount, squareSize, topRow, leftCol, bottomRow, rightCol):
	# left most point
	top_row = zeroCount[topRow][leftCol]["no_of_zeros_in_right"] >= squareSize
	left_Col = zeroCount[topRow][leftCol]["no_of_zeros_in_bottom"] >= squareSize
	
	# bottom point
	bottom_row = zeroCount[bottomRow][leftCol]["no_of_zeros_in_right"] >= squareSize
	
	# right point
	right_col = zeroCount[topRow][rightCol]["no_of_zeros_in_bottom"] >= squareSize
	
	return top_row and left_Col and bottom_row and right_col
	
def countZero(matrix):
	# create a copy of matrix: matrix will be a dict
	zeroCount = [[i for i in row] for row in matrix]
	
	# initialize every zero with : no of zero to right and number of zero to bottom
	n = len(matrix)
	
	for row in range(n):
		for col in range(n):
			numofZeros = 0 if matrix[row][col] == 1 else 1
			zeroCount[row][col] = {
				"no_of_zeros_in_bottom" : numofZeros,
				"no_of_zeros_in_right" : numofZeros
			}
			
	# fill in no of zeros to right and bottom
	for row in reversed(range(n)):
		for col in reversed(range(n)):
			if matrix[row][col] == 1:
				continue
			if row < n - 1:
				zeroCount[row][col]["no_of_zeros_in_bottom"] += zeroCount[row+1][col]["no_of_zeros_in_bottom"]
			if col < n - 1:
				zeroCount[row][col]["no_of_zeros_in_right"] += zeroCount[row][col+1]["no_of_zeros_in_right"]
	
	return zeroCount