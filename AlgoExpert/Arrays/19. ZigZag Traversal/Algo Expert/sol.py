# Time = O(row. col)
# Space = O(1) if we dont consider op else O(n)

def zigzagTraverse(array):
    height = len(array) - 1
	width = len(array[0]) - 1
	
	row = 0
	col = 0
	
	res = []
	
	goingDown = True
	
	while not isBound(row, col , height, width):
		res.append(array[row][col])
		
		# moving down:
		if goingDown:
			# Every time we hit a border we need to change direction
			if col == 0 or row == height:
				goingDown = False # From the next cell. Start going up
				
				if row == height:
					col += 1
				else:
					row += 1
			# Dont change any direction		
			else:
				row += 1
				col -= 1
		
		# going up
		else:
			if row == 0 or col == width:
				goingDown = True
				if col == width:
					row += 1
				else:
					col += 1
			else:
				row -= 1
				col += 1
	
	return res
	
	
def isBound(row, col , height, width):
	return row < 0 or col < 0 or row > height or col > width
