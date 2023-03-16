def searchForRange(array, target):
    indexes = [-1, -1]
	# First time move left to find the targets first occurance
	helper(0,len(array)-1,array,target,indexes,leftIdx = True)
	# Move to the right to find the target last occuracne
	helper(0,len(array)-1,array,target,indexes,leftIdx = False)
	
	return indexes

def helper(left,right,array,target,indexes,leftIdx):
	# Condition to stop the call
	if left > right:
		return
	
	mid = (left+right) // 2
	
	
	if target < array[mid]:
		right = mid - 1
		helper(left,right,array,target,indexes,leftIdx)
	elif target > array[mid]:
		left = mid + 1
		helper(left,right,array,target,indexes,leftIdx)
	else: # target == mid
		if leftIdx:
			# Finding first occurance of target
			if mid == 0 or array[mid-1] != target:
				indexes[0] = mid
			else:
				right = mid - 1
				helper(left,right,array,target,indexes,leftIdx)
		else:
			# Finding the last occurance of target
			if mid == len(array) - 1 or array[mid+1] != target:
				indexes[1] = mid
			else:
				left = mid + 1
				helper(left,right,array,target,indexes,leftIdx)