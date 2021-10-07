# run time O(n^2)
# space O(n)

def threeNumberSum(array, targetSum):
    array.sort() # O(nlogn)
	
	triplet = []
	
	for i in range(len(array) - 2): # o(n)
		lftIdx = i + 1
		rgtIdx = len(array) - 1
		
		# if left index cross right index we will bascially be doing same calculation again
		while lftIdx < rgtIdx:  # O(n)
			currentSum = array[i] + array[lftIdx] + array[rgtIdx]
			
			if currentSum == targetSum:
				triplet.append([array[i], array[lftIdx], array[rgtIdx]])
				lftIdx += 1
				rgtIdx -= 1
				
			elif currentSum < targetSum:
				lftIdx += 1
				
			else:
				rgtIdx -= 1
				
	return triplet