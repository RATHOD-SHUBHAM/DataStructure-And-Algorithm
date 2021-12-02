def shiftedBinarySearch(array, target):
    left = 0
	right = len(array) - 1
	
	while left <= right:
		mid = (left + right) // 2
		
		print("left: ",left)
		print("right: ",right)
		print("mid: ",mid)
		
		if array[mid] == target:
			return mid
		# here ill know if my elements from left to mid are sorted
		elif array[left] <= array[mid]:
			if target >= array[left] and target < array[mid]:
				right = mid - 1
			else:
				left = mid + 1
		else:
			# here Ill know my elements from mid to last are sorted
			if target <= array[right] and target > array[mid]:
				left = mid + 1
			else:
				right = mid - 1
	return -1