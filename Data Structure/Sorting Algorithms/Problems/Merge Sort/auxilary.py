# using acopy of main array and sorting on it using pointer will save memory
# Time complexity = O(n log n)
# Space Complexity = O(n)

def mergeSort(array):
    # Write your code here.
	if len(array) <= 1:
		return array
	
    aux = array[:]
	
	left = 0 
	right = len(array) - 1
	
	merge(array, left, right, aux)
	
	return array

def merge(array, left, right,aux):
	if left == right:
		return
	
	mid = (left + right) // 2
	
	merge(aux,left,mid,array)
	merge(aux,mid+1,right,array)
	
	mergeArray(array, left, mid, right, aux)

def mergeArray(array,left, mid, right, aux):
	i = left
	j = mid + 1
	k = left
	
	while i <= mid and j <= right:
		if aux[i] < aux[j]:
			array[k] = aux[i]
			i += 1
		else:
			array[k] = aux[j]
			j += 1
		k += 1
		
	# if any elements are presnt in aux array that is not been added.
	# add them
	
	while i <= mid:
		array[k] = aux[i]
		i += 1
		k += 1
		
	while j <= right:
		array[k] = aux[j]
		j += 1
		k += 1
		
	return array
		
	