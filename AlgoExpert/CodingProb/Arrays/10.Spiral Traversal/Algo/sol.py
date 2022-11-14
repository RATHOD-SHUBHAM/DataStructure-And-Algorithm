# Time = O(n), where n is no of element in array
# Space = O(1)

def spiralTraverse(array):
	# 4 pointer
	left  = top = 0
	right = len(array[0])
	bottom = len(array)
	
	# to store result
	op = []
	
	# enter the loop
	while top < bottom and left < right:
		
		# move from left to right
		for i in range(left, right):
			op.append(array[top][i])

		top += 1
		# print(op)

		# if i had only one row:
		if top == bottom:
			break

		# move from top to bottom on right col
		for i in range(top, bottom):
			op.append(array[i][right-1])

		right -= 1
		# print(op)

		# if i had only one col.
		if left == right:
			break
			
		# move from right to left
		for i in reversed(range(left, right)):
			op.append(array[bottom - 1][i])
		
		bottom -= 1
		# print(op)
		
		# move from bottom to up
		for i in reversed(range(top, bottom)):
			op.append(array[i][left])
		
		left += 1
		# print(op)
		
	return op
			
		
