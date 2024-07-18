# Time Complexity = O(n+m)
# n = no of row
# m = no of column
# space complexity = O(1)

def searchInSortedMatrix(matrix, target):
    row = 0
	col = len(matrix[0]) - 1
	
	while row < len(matrix) and col >= 0 :
		if matrix[row][col] == target:
			return([row,col])
		elif matrix[row][col] > target:
			col -= 1
		elif matrix[row][col] < target:
			row += 1
			
	return([-1,-1])
