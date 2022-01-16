# Time and Space = O(1)

def solveSudoku(board):
    solvePartialSudoku(0,0,board)
    return board

def solvePartialSudoku(row,col,board):
	curRow = row
	curCol = col
	print("curRow: ", curRow)
	print("curCol : ",curCol)
	# if I reach the end of column --> ill move to next row
	if curCol == len(board[row]):
		curRow += 1
		curCol = 0
		# if i reach the end. then I have filled up my board
		if curRow == len(board):
			return True # for sure there will be a solution
		
	if board[curRow][curCol] == 0:
		op =  tryDigit(curRow, curCol, board)
		print("op: ",op)
		return op
	
	# if i have added a valid number at current position move to next col
	oP = solvePartialSudoku(curRow, curCol+1, board)
	print("oP : ",oP)
	return oP

def tryDigit(row,col,board):
	for i in range(1,10):
		if isValidAtPosition(i, row,col, board):
			board[row][col] = i
			print("board[row][col] : ",board[row][col])
			# if this is a valid number add the number on baord and move to next col
			if solvePartialSudoku(row, col+1, board):
				return True
	print("here")		
	board[row][col] = 0
	return False

def isValidAtPosition(val, row, col, board):
	# check if the value is present in entire 2*2 matrix
	rowIsValid = val not in board[row]
	colIsValid = val not in map(lambda x : x[col], board)
	
	# if the number is already present in particular row and column
	if not rowIsValid or not colIsValid:
		return False
	
	# check the subgrid
	# board is made of 9 --> 3x3 board
	subGridRow = (row // 3) * 3
	subGridCol = (col // 3) * 3
	
	for rowIdx in range(3):
		for colIdx in range(3):
			rowCell = subGridRow + rowIdx
			colCell = subGridCol + colIdx
			
			existingVal = board[rowCell][colCell]
			
			if existingVal == val:
				return False
			
	return True