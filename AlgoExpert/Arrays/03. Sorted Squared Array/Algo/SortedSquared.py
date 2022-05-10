# Time and space = O(n)
def sortedSquaredArray(array):
	result = [1] * len(array)
	
	left = 0
	right = i = len(array) - 1
	
	while left <= right:
		sqrt_left = array[left]**2
		sqrt_right = array[right]**2
		
		if sqrt_left < sqrt_right:
			result[i] = sqrt_right
			right -= 1
		else:
			result[i] = sqrt_left
			left += 1
			
		i -= 1
		
	return result