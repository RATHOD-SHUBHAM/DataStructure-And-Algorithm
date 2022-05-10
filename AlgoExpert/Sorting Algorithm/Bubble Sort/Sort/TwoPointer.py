# Time Complexity = O(n)
# Space Complexity = O(1)

def bubbleSort(array):
    left = 0
	right = len(array) - 1
	
	while left < right:
		if array[left] > array[left+1]:
			array[left], array[left + 1] = array[left + 1], array[left]
			
		left += 1
		
		if left == right:
			right -= 1
			left = 0
			
			
	return array
