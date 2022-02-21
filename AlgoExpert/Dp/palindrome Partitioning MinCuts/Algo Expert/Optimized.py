# Time = O(n^2)
# Space = O(n^2)

import math
def palindromePartitioningMinCuts(string):
    dp = [[False for _ in range(len(string))] for _ in range(len(string))]
	
	# make the diagonals true
	for i in range(len(string)):
		dp[i][i] = True
		
	# Check palindrome for sub array
	for length in range(2,len(string) + 1): #subarray will have atleast 2 element
		for i in range(0 , len(string) - length + 1):
			j = i + length - 1 # 0 + 2: index should be 1 so -1
			
			if length == 2:
				dp[i][j] = string[i] == string[j]
			else:
				dp[i][j] = string[i] == string[j] and dp[i+1][j-1]
	
	# print(dp)
	
	minCuts = [math.inf for _ in range(len(string))]
	
	for i in range(len(string)):
		if dp[0][i]:
			minCuts[i] = 0
		else:
			minCuts[i] = minCuts[i-1] + 1
			for j in range(1,i):
				if dp[j][i] and minCuts[j-1] + 1 < minCuts[i]:
					minCuts[i] = minCuts[j-1] + 1
	return minCuts[-1]