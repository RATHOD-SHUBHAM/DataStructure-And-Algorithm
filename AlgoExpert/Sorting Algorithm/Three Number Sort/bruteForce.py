# Brute Force Approach

# Time Complexity = O(n^2)
# Space Complexity = O(1)

def threeNumberSort(array, order):
	left = 0
	right = 1
	i = 0
	sortNumber(array,order,left,right,i)
	return array
	
def sortNumber(array,order,left,right,i):
	if i < len(array):
		while right < len(array):
			if array[right] == order[i] and array[left] != order[i]:
				array[left], array[right] = array[right], array[left]
				left += 1
				right += 1

			elif array[right] != order[i] and array[left] != order[i]:
				right += 1

			elif (array[right] == order[i] and array[left] == order[i]) or (array[right] != order[i] and array[left] == order[i]) :
				left += 1
				right += 1

		i += 1
		sortNumber(array,order,left,left+1,i)

	else:
		return
				
				
				
		
				
		
			
