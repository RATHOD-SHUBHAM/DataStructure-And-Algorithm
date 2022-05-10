# Time and Space = O(n) | O(n)

def maxSubsetSumNoAdjacent(array):
    if len(array) == 0:
		return 0
	elif len(array) == 1:
		return array[0]
	else:
		maxSum = array[:]
		maxSum[1] = max(maxSum[0], maxSum[1])
		
		for i in range(2,len(array)):
			maxSum[i] = max(maxSum[i-1], maxSum[i-2] + array[i])
			
			
		return maxSum[-1]
	
	