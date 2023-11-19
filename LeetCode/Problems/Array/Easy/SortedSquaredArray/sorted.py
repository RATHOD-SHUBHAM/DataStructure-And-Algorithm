# time complexity = O(n)
# space complexity = O(n)

def sortedSquaredArray(array):
    sorted_array = [0] * len(array)
	
	small = 0
	large = len(array) - 1
	
	for i in reversed(range(len(array))):
		if abs(array[small]) < abs(array[large]):
			sorted_array[i] = array[large] * array[large]
			large -= 1
		else:
			sorted_array[i] = array[small] * array[small]
			small += 1
			
	return sorted_array
