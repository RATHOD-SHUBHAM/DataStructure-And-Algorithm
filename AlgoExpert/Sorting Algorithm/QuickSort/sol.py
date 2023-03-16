# Time Complexity = O(nlog(n))
# space Complexity = O(log(n))


def quickSort(array):
    helper( array, 0, len(array)-1 )
	return array

def helper(array, startIdx, endIdx):
	
	# when there is only one element
	if startIdx >= endIdx:
		return
	
	
	pivot = startIdx
	left = pivot + 1
	right = endIdx
	
	
	while right >= left:
	
		# This will make sure that all the element on left is less than pivot.
		# and all the elements on the right is greater than pivot.
		if array[left] > array[pivot] and array[right] < array[pivot]:
			swap(array,left,right)

		# if the left element is less than pivot. Dont do anything. Just move forward
		if array[left] <= array[pivot]:
			left += 1

		# if the right element is greater than pivot. Dont do anything. Just move backward
		if array[right] >= array[pivot]:
			right -= 1
			
	# once left has crossed right then
	swap(array,pivot,right)
	
	
	# Find out the smallest subarray
	# so after the final Swap. our right pointer element and pivot element got swapper
	# but the pointers are still in its position. ie pivot will be in start and right pointer somewhere in btn
	# so all the elements on left of right pointer are smaller than right pointer element
	# and all the elements on right of right pointer are greater than right pointer element
	
	smallSubArray = (right - 1) - startIdx < endIdx - (right + 1)
	
	# if left sub array is small
	if smallSubArray:
		helper(array,startIdx, right - 1)
		helper(array,right + 1,endIdx)
		
	else:
		helper(array,right + 1,endIdx)
		helper(array,startIdx, right - 1)
		
		
def swap(array,left,right):
	array[left], array[right] = array[right], array[left]
