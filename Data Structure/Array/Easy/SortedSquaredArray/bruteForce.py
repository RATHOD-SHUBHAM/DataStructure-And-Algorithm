# time Complexity: O(nlog(n))
# space Complexity: O(1)

def sortedSquaredArray(array):
	for i in range(len(array)):
		array[i] *= array[i]
		
	array.sort()
	return array