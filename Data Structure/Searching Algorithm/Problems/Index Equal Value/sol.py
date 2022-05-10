'''
Find the First index which is equal to its value

so when mid == index we have to check its previous element as well



Cases: 
1. when index > value

  0
[-1]  --> in this case all the element on left of the index will never match the index

2. When index < value
 4
[5] --> in this case all the element on right will never match the index

3. When index match the value but that is not the first index to match value
  0.  1. 2
[ 0 , 1, 2]

this time our mid will be 1 and it matches the index. 
But that is not the first one.
So we got to check the previous indexes as well


'''

def indexEqualsValue(array):
    left = 0
	right = len(array) - 1
	return helper(left,right,array)

def helper(left,right,array):
	while left <= right:
		mid = (left + right) // 2
		
		# check if this was the first time where index match the value
		if array[mid] == mid and array[mid-1] != mid-1:
			return mid
		elif array[mid] == mid and mid == 0:
			return mid
		
		# Check if my index is small then value
		# also if index is same as value but there are other elements with same index and value before it
		if mid <= array[mid]:
			right = mid - 1
		elif mid > array[mid]:
			left = mid + 1
			
	return -1