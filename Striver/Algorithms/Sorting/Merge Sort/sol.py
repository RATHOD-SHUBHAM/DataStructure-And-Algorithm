def mergeSort(array):
    # Write your code here.
    if len(array) == 1:
        return array

    mid = len(array) // 2

    leftArray = array[:mid]
    rightArray = array[mid:]

    sortedArray = mergeArray(mergeSort(leftArray), mergeSort(rightArray))
    return sortedArray


def mergeArray(leftArray,rightArray):
	
	sortedArray = [None] * (len(leftArray) + len(rightArray))
	
	i = k = j = 0 
	
	while i < len(leftArray) and j < len(rightArray):
		if leftArray[i] < rightArray[j]:
			sortedArray[k] = leftArray[i]
			i += 1
		else:
			sortedArray[k] = rightArray[j]
			j += 1
		k += 1
		
	while i < len(leftArray):
		sortedArray[k] = leftArray[i]
		i += 1
		k += 1
			
	while j < len(rightArray):
		sortedArray[k] = rightArray[j]
		j += 1
		k += 1

	return sortedArray
	
	
