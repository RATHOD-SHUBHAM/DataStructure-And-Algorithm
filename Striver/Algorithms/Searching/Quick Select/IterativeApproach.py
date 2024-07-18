# Time complexity = O(n)
# Space Complexity = O(log(n))

def quickselect(array, k):
    pos = k - 1
	return helper(array,0,len(array)-1,pos)
	 
def helper(array, startIdx,endIdx,pos):
	while True:
		if startIdx > endIdx:
			break
			
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
				
		swap(array, pivot, right)
		
		if right == pos:
			return array[pos]
		elif right > pos:
			endidx = right - 1
		else:
			startIdx = right + 1
			
def swap(array,left,right):
	array[left], array[right] = array[right],array[left]
