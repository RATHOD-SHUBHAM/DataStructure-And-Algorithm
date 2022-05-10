'''
										no of ways to reach the upper cell
No of ways to reach a particular cell = 	+
										no of ways to reach he left cell

And for cell with height and width = 1, there is only one way to reach
'''
# time and space = O(m + n)
def numberOfWaysToTraverseGraph(width, height):
	# add extra zero on top and left to prevent list index overflow
    dp = [[0 for _ in range(width + 1)] for _ in range(height+1)]
	
	for i in range(1,height+1):
		for j in range(1, width+1):
			if i == 1 and j == 1:
				dp[i][j] = 1
			else:
				waysUp = dp[i-1][j]
				waysLeft = dp[i][j-1]
				dp[i][j] = waysUp + waysLeft
	return dp[height][width]