# Time Complexity = O(n)
# Space Complexity = O(1)

def bubbleSort(array):
    left = 0
	right = len(array) - 1
	helper(array,left,right)
	return array
	
def helper(array,left,right):
	while left < right:
		if array[left] > array[left+1]:
			swap(array,left,left+1)
			
		left += 1
		
		if left == right:
			right -= 1
			left = 0
			
def swap (array, left,right):
	array[left], array[right] = array[right], array[left]