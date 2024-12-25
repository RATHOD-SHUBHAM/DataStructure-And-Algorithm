# Time complexity = O(n)
# Space Complexity = O(log)n

def quickselect(array, k):
	pos = k - 1
	helper(array,0,len(array)-1,pos)
	return array[pos]
	 
def helper(array, startIdx,endIdx,pos):
	
	if startIdx > endIdx:
		raise Exception("Error")

	pivot = startIdx
	left = pivot + 1 
	right = endIdx
	

	while left <= right:
	
		if array[left] > array[pivot] and array[right] < array[pivot]:
			swap(array,left,right)
			print(array)

		if array[left] <= array[pivot]:
			left += 1

		if array[right] >= array[pivot]:
			right -= 1
	
	swap(array, pivot, right)
	


	if right == pos:
		return
	elif right > pos:
		helper(array,startIdx,right - 1,pos)
	else:
		helper(array,right + 1,endIdx,pos)
			
def swap(array,left,right):
	array[left], array[right] = array[right],array[left]
