# Time = O(nd)
# space = O(n)
def minNumberOfCoinsForChange(n, denoms):
    dp = [float("inf")] * (n+1)
	
	dp[0] = 0
	
	for x in range(1, n+1):
		for y in denoms:
			if y <= x:
				dp[x] = min(dp[x] , 1 + dp[x-y])
	return dp[n] if dp[n] != float("inf") else -1
