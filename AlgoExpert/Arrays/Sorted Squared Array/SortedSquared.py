# Time Complexity = o(n) => as it goes through entire array
# n is the length of input array

# Space Complexity = o(n) => as we are creating new array
def sortedSquaredArray(array):
	# initialize a new array of same length as input array so as to store the square root in sorted order
    res = [0] * len(array)
	# res = [0 for _ in array]
	smallIdx = 0
	largeIdx = len(array)-1
	
	# store the array i descending order (from the back).
	# So while reading it form the front it will be in sorted or ascending order.
	for i in reversed(range(len(array))):
		largeVal = array[largeIdx]
		smallVal = array[smallIdx]
		
		if abs(smallVal) < abs(largeVal):
			res[i] = largeVal * largeVal
			largeIdx -= 1
			
		else:
			res[i] = smallVal * smallVal
			smallIdx += 1
    return res
