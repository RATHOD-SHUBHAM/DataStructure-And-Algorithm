# https://leetcode.com/problems/house-robber/discuss/1753812/Maximum-Sum-of-Non-Adjacent-Elements-or-O(1)

# Time and space = O(n) | O(1)

def maxSubsetSumNoAdjacent(array):
    if len(array) == 0:
		return 0
	elif len(array) == 1:
		return array[0]
	else:
		maxSum = array[:2]
		maxSum[1] = max(maxSum[0], maxSum[1])
		
		for i in range(2,len(array)):
			curSum = max(maxSum[1], maxSum[0] + array[i])
			maxSum[0] = maxSum[1]
			maxSum[1] = curSum
			
		return maxSum[1]

# or

'''
# using 2 variables

def maxSubsetSumNoAdjacent(array):
    if len(array) == 0:
		return 0
	elif len(array) == 1:
		return array[0]
	else:
		nonNeighborSum = array[0]
		neighborSum = max(array[0], array[1])
		
		for i in range(2,len(array)):
			curSum = max(neighborSum , nonNeighborSum + array[i])
			nonNeighborSum = neighborSum
			neighborSum = curSum
		return neighborSum



'''