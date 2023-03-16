# Normal Merge Sort:
# Time Complexity = O(n log n)
# Space Complexity = O(n log n)

def mergeSort(array):
	# check the base case as well as the recursive case
    if len(array) <= 1:
		return array
	
	mid = len(array) // 2
	
	# creating a left and right array takes space
	'''
	# Single Liner
	
	leftArray = [:mid]
	rightArray = [mid:]
	
	return mergeArray(mergeSort(leftArray), mergeSort(rightArray))
	
	'''
	left = array[:mid]
	right = array[mid:]

	leftArray = mergeSort(left)
	rightArray = mergeSort(right)
	
	sortedArray = mergeArray(leftArray, rightArray)
	
	return sortedArray

def mergeArray(left,right):
	# creating a seperate array to store store sorted array
	sortedArray = [0] * (len(left) + len(right))
	
	# pointer for left right and sorted array
	i = j = k = 0
	
	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			sortedArray[k] = left[i]
			i += 1
		else:
			sortedArray[k] = right[j]
			j += 1
		k += 1
		
	# add the remaining element of the array into the sorted array
	# as they would be in sorted order
	while i < len(left):
		sortedArray[k] = left[i]
		i += 1
		k += 1
	
	while j < len(right):
		sortedArray[k] = right[j]
		j += 1
		k += 1
	
	return sortedArray