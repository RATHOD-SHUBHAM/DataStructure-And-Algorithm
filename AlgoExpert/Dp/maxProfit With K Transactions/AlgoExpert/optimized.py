# Time = O(nk)
# space = O(n)

import math
def maxProfitWithKTransactions(prices, k):
	if not prices:
		return 0
	
	# part of dp array
    even = [0 for _ in range(len(prices))]
	odd = [0 for _ in range(len(prices))]
	
	# loop through transaction
	for i in range(1 , k+1):
		if i % 2 == 0:
			cur = even
			prev = odd
		else:
			cur = odd
			prev = even
			
		maxProfit = -math.inf
		# loop through prices
		for j in range(1,len(prices)):
			maxProfit = max(maxProfit, -prices[j-1] + prev[j-1])
			cur[j] = max(cur[j-1], prices[j] + maxProfit)
			
	if k % 2 == 0:
		return even[-1]
	else:
		return odd[-1]