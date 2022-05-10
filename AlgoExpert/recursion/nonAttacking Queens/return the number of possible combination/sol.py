# time = O(n!)
# space = O(n)
def nonAttackingQueens(n):
	# each index is considered to be a row
    queenTracker = [0] * n # keep track of col in which queen is placed
    return correctPlacment(0,n,queenTracker)

def correctPlacment(row,n,queenTracker):
	# base case: when i move out of the last row. I have finished placing every queen in right position
	if row == n:
		return 1
	
	validPlacmentCount = 0
	
	for col in range(n):
		if isValidPlace(row,col,queenTracker):
			queenTracker[row] = col
			validPlacmentCount += correctPlacment(row + 1,n,queenTracker)
			
	return validPlacmentCount
		
# check if there are no queen in particular col and in diagonal col
def isValidPlace(row,col,queenTracker):
	for aboveRow in range(row):
		colToCheck = queenTracker[aboveRow]
		
		# check if they are in same col
		sameCol = False
		if col == colToCheck:
			sameCol = True
		'''
		This can be written as
		sameCol = (col == colToCheck)
		'''
			
		# check diagonal => abs(x2 - x1) = abd(y2 - y1)
		sameDiagonal = False
		if abs(col - colToCheck) == abs(row - aboveRow):
			sameDiagonal = True
			
		if sameCol or sameDiagonal:
			return False
		
	return True
