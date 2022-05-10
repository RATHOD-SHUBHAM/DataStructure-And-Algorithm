def mergeSort(array):
	if len(array) <= 1:
		return array
	
	left = 0
	right = len(array)
	return mergeSortAlgo(left,right,array)

def mergeSortAlgo(start,end,array):
	if end - start <= 1:
		return 0
	
	mid = start + (end - start) // 2
	
	leftArray = mergeSortAlgo(start,mid,array)
	rightArray = mergeSortAlgo(mid,end,array)
	
	mergeArray(start,mid,end,array)
	
	return array

def mergeArray(start,mid,end,array):
	sortedArray = []
	
	i = start
	j = mid
	
	while i < mid and j < end:
		if array[i] < array[j]:
			sortedArray.append(array[i])
			i += 1
		else:
			sortedArray.append(array[j])
			j += 1
			
	sortedArray += array[i:mid] + array[j:end]
	
	for idx, num in enumerate(sortedArray):
		array[start + idx] = num
		
	return array
