# Time = O(c.a) C = coins, a = amount
# Space = O(a)
def minNumberOfCoinsForChange(amounts, coins):
	dp = [float("inf")] * (amounts+1)
	
	# to make 0$ i dont need any coin
	dp[0] = 0
	
	
	for coin in coins:
		for amount in range(1, (amounts+1)):
			# coin = 1 and amount = 1
			# i can make amount of 1$ if i have coin <= 1$
			if coin <= amount:
				# Coin + no of note to make remaining amount
				dp[amount] = min(dp[amount] , 1 + dp[amount - coin])
	# 			print(dp)
	# 	print("\n")
	# print("\n")
	# print(dp)
	return dp[amounts] if dp[amounts] != float("inf") else -1 