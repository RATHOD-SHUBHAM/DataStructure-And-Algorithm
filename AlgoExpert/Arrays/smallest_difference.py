# time = O(nlogn + mlogm)
# space = O(1) # not adding any memeory just keeping track of existing variables.
def smallestDifference(arrayOne, arrayTwo):
    
	arrayOne.sort() # O(nlogn)
	arrayTwo.sort() # O(mlogm)
	
	num = [] # store the number
	
	mini = float('inf') # keep track of minimum difference
	
	idxOne, idxTwo = 0 , 0 
	
	while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
		firstNum = arrayOne[idxOne]
		secondNum = arrayTwo[idxTwo]
		
		abs_difference  = abs(firstNum - secondNum)
		
		if firstNum < secondNum:
			idxOne += 1
		elif secondNum < firstNum:
			idxTwo += 1
		else:
			return [firstNum, secondNum] # abs_difference = 0
		
		if abs_difference < mini:
			mini = abs_difference
			num = [firstNum, secondNum] # update the num value to current firstNum, secondNum
			
	return num
	
	
