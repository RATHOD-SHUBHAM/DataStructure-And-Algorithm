# Time Complexity = O(log(n))
# Space Complexity = O(1)


def shiftedBinarySearch(array, target):
    l = 0
	r = len(array) - 1
	
	while l <= r:
		# calculate mid point
		mid = (l + r) // 2
		
		if target == array[mid]:
			return mid
		
		# Assure my elements from are in sorted form from left to middle
		elif array[l] <= array[mid]:
			# my element is between left and mid
			if target >= array[l] and target < array[mid]:
				r = mid - 1
			else: # my element is not between left and mid
				l = mid + 1
				
		# if the elements are not in sorted order from left to mid 
		else: # this also means that elements are sorted from mid to right
			if target > array[mid] and target <= array[r]:
				l = mid + 1
			else:
				r = mid - 1
				
	return -1
			
		
			
		
