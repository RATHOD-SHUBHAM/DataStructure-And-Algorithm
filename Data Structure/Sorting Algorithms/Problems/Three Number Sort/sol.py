def threeNumberSort(array, order):
    # Write your code here.
    firstEle = order[0]
	lastEle = order[2] # array with three distinct integer	
	
	# pointers
	left = 0
	right = len(array) -1 
	
	# putting the first number in right position
	for i in range(len(array)):
		if array[i] == firstEle:
			swap(i,left,array)
			left += 1
	# print(array)
	
	# putting the last element in right position
	for i in reversed(range(len(array))):
		if array[i] == lastEle:
			swap(i,right,array)
			right -= 1
	# print(array)
	return array

def swap(left,right,array):
	array[left], array[right] = array[right], array[left]