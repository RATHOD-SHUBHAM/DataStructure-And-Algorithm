# Time Complexity = O(nlogn)
# Space Complexity = O(logn)

# sort the array and then return the kth element from the array
def quickselect(array, k):
	helper(array,0,len(array)-1)
	return array[k-1]

def helper(array,startIdx,endIdx):
	
	if startIdx > endIdx:
		return
	
	pivot = startIdx
	left = pivot + 1
	right = endIdx
	
	while left <= right:
		if array[left] > array[pivot] and array[right] < array[pivot]:
			swap(array,left,right)
			
		if array[left] <= array[pivot]:
			left += 1
			
		if array[right] >= array[pivot]:
			right -= 1
			
		
	swap(array,pivot,right)
	
	smallSubarray = (right - 1) - startIdx < endIdx - (right + 1)
	
	if smallSubarray:
		helper(array,startIdx,right-1)
		helper(array,right+1,endIdx)
	else:
		helper(array,right+1,endIdx)
		helper(array,startIdx,right-1)
		
def swap(array,left,right):
	array[left],array[right] = array[right],array[left]
