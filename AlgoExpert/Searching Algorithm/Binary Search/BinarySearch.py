# Binary Search: Split the array into half for each traversal.
# time Complexity = O(n)
# Space Complexity = O(1)

def binarySearch(array, target):
	left = 0
	right = len(array) - 1
    return helper (array,target,left,right)

def helper(array,target,left,right):
	# did not find the match, return -1
	if left > right:
		return -1
	
	mid = (left + right) //2
	
	# found the element so return index
	if array[mid] == target:
		return mid
	elif array[mid] < target:
		left = mid + 1
		return helper(array,target,left,right)
	else:
		right = mid - 1
		return helper(array,target,left,right)
	
