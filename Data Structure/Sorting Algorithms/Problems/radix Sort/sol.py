"""
Order of the elements in array is really important.
We just cant swap them.

1. Find out the largest number in the array and figure out how many digit it has.
10 ** 0 = 10 ^ 0 = 1
10 ^ 1 = 10 etc

2. As long I have numbers in my maxNumber ill call the count sort.


# Counting Sort()

Count = len of base number system
Sorted = len of array


1] Increase count in a countArray for each digit
2] Add those count in countarray so that you can place the element at right position 
3] Move in backward direction of the given array, remove a value from count array, 
then at that position place the element of the array
4] Copy the sorted array to main array
"""

def radixSort(array):
    # base case
	if len(array) <= 1:
		return array
	
	# get the max number form array
	maxNumber = max(array)
	# print("The max number is: ",maxNumber)
	
	
	# as long as we have elements in the max number keep performing counting sort
	# 8762 = 4
	digit = 0
	while maxNumber / 10 ** digit > 0:
		countSort(array,digit)
		digit += 1
		
	return array

def countSort(array,digit):
	print(array)
	# creating a sorted array 
	sortedArray = [0] * len(array)
	
	# create a array that will hold the count
	# multiplying by 10. because we are using base 10 decimanl system
	countArray = [0] * 10
	
	#get the place of digit. eg. unit(1) 10 100 etc
	digitPlace = 10 ** digit
	
	for num in array:
		# Extract the digitplace element
		countIdx = (num // digitPlace ) % 10
		# print("CountIdx = ",countIdx)
		# Increase the count value at the countArray
		countArray[countIdx] += 1
		
	# print("CountArray",countArray)
	
	# Fill up the space so that we can keep adding the number before the sorted element
	for idx in range(1,10):
		countArray[idx] += countArray[idx - 1]
	# print("CountArray",countArray)
	
	# Move in backwared direction
	for idx in range(len(array)-1, -1, -1):
		# Take the digit number from the array
		countIdx = (array[idx] // digitPlace) % 10
		
		# Now subtract one number from countArray
		countArray[countIdx] -= 1
		
		# now add the array element at the position of the digitPlace in countArray
		sortedIdx = countArray[countIdx]
		sortedArray[sortedIdx] = array[idx]
		
		
	# copy the sorted array to main array
	
	for idx in range(len(array)):
		array[idx] = sortedArray[idx]
		
	return array
	
	
	
		