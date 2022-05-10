# Time and space = O(nk) 

import math
def maxProfitWithKTransactions(prices, k):
    if not prices:
		return 0
	
	profit = [[0 for _ in range(len(prices))] for _ in range(k+1)]
	
	# loop for transaction
	for i in range(1,k+1):
		# keep track of max profit
		maxProfit = -math.inf
		# loop through prices
		for j in range(1,len(prices)):
			maxProfit = max(maxProfit, -prices[j-1] + profit[i-1][j-1])
			profit[i][j] = max(profit[i][j-1], prices[j] + maxProfit)
	
	return profit[-1][-1]
