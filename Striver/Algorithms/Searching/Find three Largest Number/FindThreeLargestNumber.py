# ip = [-2, -1, 7]
# so I cant keep zeros in my threeLargest

def findThreeLargestNumbers(array):
	threeLargest = [None,None,None]
	
	for num in array:
		if threeLargest[2] is None or num > threeLargest[2] :
			update_3_largest(threeLargest, num,2)
		elif threeLargest[1] is None or num > threeLargest[1]:
			update_3_largest(threeLargest, num,1)
		elif threeLargest[0] is None or num > threeLargest[0]:
			update_3_largest(threeLargest, num,0)
			
	return threeLargest
			