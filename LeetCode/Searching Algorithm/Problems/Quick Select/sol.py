def quickselect(array, k):
    pos = k - 1
	return helper(0,len(array)-1,array,pos)

def helper(start,end,array,pos):
	# this part is like quick sort
	while start <= end:
		pivot = start
		left = start + 1
		right = end
		
		while left <= right:
			if array[left] > array[pivot] and array[right] < array[pivot]:
				swap(array,left,right)
			if array[left] <= array[pivot]:
				left += 1
			if array[right] >= array[pivot]:
				right -= 1
		swap(array,pivot,right)
		
		# this part is like binary search
		if array[right] == array[pos]:
			return array[right]
		elif pos < right:
			end = right - 1
			helper(start,end,array,pos)
		else:
			start = right + 1
			helper(start,end,array,pos)
			
def swap(array,left,right):
	array[left], array[right] = array[right], array[left]