'''
Order = [0,1,-1]


1. First put all the 0 to begining of array

2. Then put all the -1 to end of the array
In this way all the 1 will come in middle of the array

'''

# Time Complexity = O(n)
# Space Complexity = O(1)
def threeNumberSort(array, order):
    firstEle = order[0]
	lastEle = order[-1] #order[2]
	
	firstIdx = 0
	lastIdx = len(array) - 1
	
	for i in range(len(array)):
		if array[i] == firstEle:
			array[i], array[firstIdx] = array[firstIdx], array[i]
			firstIdx += 1
			
	for i in reversed(range(len(array))):
		if array[i] == lastEle:
			array[i], array[lastIdx] = array[lastIdx], array[i]
			lastIdx -= 1
			
	return array
