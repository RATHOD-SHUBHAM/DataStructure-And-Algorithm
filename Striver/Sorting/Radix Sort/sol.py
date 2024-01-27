def radixSort(array):
    # base case
	if len(array) <= 1:
		return array
	
	maxNum = max(array)
	
	# count nuber of element in maxNum
	digit = 0
	while maxNum / 10 ** digit > 0:
        # CountSort
		countSort(array,digit)
		digit += 1
	
	return array


def countSort(array,digit):
    # step 1
    sortedArray = [0] * len(array)

    countArray = [0] * 10

    # place holder = Unit place, 10th or 100 and so on
    digitPlace = 10 ** digit

    # Step 2: Count the number of times digit has occured
    for num in array:
        countIdx = (num // digitPlace ) % 10
        
        countArray[countIdx] += 1
        
    # Step 3: Determine where to place elements in a partially sorted array
    # Fill up the space so that we can keep adding the number before the sorted element
    for i in range(1,10):
        countArray[i] += countArray[i - 1]
        
    # Step 4: Move in backward direction of the given array
    # for idx in range(len(array) - 1,-1,-1):
    for idx in reversed(range(len(array))):
        countIdx = (array[idx] // digitPlace) % 10
        
        countArray[countIdx] -= 1
        
        sortedIdx = countArray[countIdx]
        
        sortedArray[sortedIdx] = array[idx]
        
    # step 5: copy the sorted array to main array	
    for i in range(len(array)):
        array[i] = sortedArray[i]

    return array
