# Time Complexity = O(n log n)
# Sapce Complexity = O(1)

def nonConstructibleChange(coins):
    currentChange = 0
	
	coins.sort()
	
	for coin in coins:
		if coin > currentChange + 1:
			return currentChange + 1
		
		currentChange += coin
	return currentChange + 1