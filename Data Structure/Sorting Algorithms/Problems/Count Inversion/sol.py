def countInversions(array):
	if len(array) <= 1:
		return 0
	
    left = 0
	right = len(array)
	return mergeSort(left,right,array)

def mergeSort(start,end,array):
	if end - start <= 1:
		return 0
	
	mid = start + (end - start) // 2
	
	leftArray = mergeSort(start,mid,array)
	rightArray = mergeSort(mid,end,array)
	
	inversion = mergeArray(start,mid,end,array)
	
	return leftArray + inversion + rightArray

def mergeArray(start,mid,end,array):
	sortedArray = []
	left = start
	right = mid
	inversion = 0
	
	while left < mid and right < end:
		if array[left] <= array[right]:
			sortedArray.append(array[left])
			left += 1
		else:
			inversion += mid - left
			sortedArray.append(array[right])
			right += 1
			
	sortedArray += array[left : mid] + array[right:end]
	
	for idx,num in enumerate(sortedArray):
		array[start + idx] = num
	
	return inversion
