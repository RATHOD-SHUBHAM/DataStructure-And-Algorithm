# Time and Space = O(n) | O(1)
def subarraySort(array):
    minVal = float("inf")
	maxVal = float("-inf")
	
	# get the minimum and maximum value that is out of bound
    for i in range(len(array)):
		# Check if the cur element is in bound.
		if isBound(i, array) == False: # if not inBound
			minVal = min(minVal, array[i])
			maxVal = max(maxVal, array[i])
	
	# if the entire array is already sorted
	if minVal == float("inf"):
		return [-1, -1]
	
	# getting the corrrect idx of min value
	start_idx = 0
	while minVal >= array[start_idx]:
		start_idx += 1
	
	# getting the corrrect idx of max value
    end_idx = len(array) - 1
	while maxVal <= array[end_idx]:
		end_idx -= 1
		
		
	return [start_idx , end_idx]

			
def isBound(i, array):
	if i == 0:
        return array[i] <= array[i+1]
    elif i == len(array) - 1:
        return array[i - 1] <= array[i]
    else:
        return array[i-1] <= array[i] <= array[i+1]