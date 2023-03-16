# Since the value is sorted:
# 1. if the value is less that index --> all elements on the left will not have index that match the value
# 2. if the value is greater than index --> all the elements on the right will nont have index that will match the value


# time complexity = O(log(n))
# Space complexity = O(1)


def indexEqualsValue(array):
	
	startIdx = 0
	endIdx = len(array) - 1
	
	return helper(array,startIdx,endIdx)
	
def helper(array,startIdx,endIdx):
	left = startIdx
	right = endIdx
	
	while left <= right:
		mid = (left + right) // 2
		
# 		print("left: ",left)
	
# 		print("right: ",right)
		
# 		print("mid: ",mid)
		
# 		print("\n")
	
		value = array[mid]
		
		if mid > value:
			left = mid + 1
		elif mid == value and mid == 0:
			return mid
		elif mid == value and mid - 1 > array[mid -1]:
			return mid
		else:
			right = mid - 1 
			
	return -1
	
