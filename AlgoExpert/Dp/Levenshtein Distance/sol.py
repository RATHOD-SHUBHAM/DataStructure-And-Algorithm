# leetcode question 72: Edit distance
# time and space = O(mn)

def levenshteinDistance(str1, str2):
    dp = [[0 for _ in range(len(str2)+1)] for _ in range(len(str1)+1)]
	
	# adding element in last row
	for i in range(len(str2) + 1):
		# dp[row][col] = dp[lastrow][col]
		dp[len(str1)][i] = len(str2) - i
		
	# adding element in last col
	for j in range(len(str1) + 1):
		dp[j][len(str2)] = len(str1) - j
		
	# levenshtein distance = bottom up approach
	for i in reversed(range(len(str1))):
		for j in reversed(range(len(str2))):
			if str1[i] == str2[j]:
				dp[i][j] = dp[i+1][j+1]
			else:
				dp[i][j] = 1 + min(dp[i][j+1] , dp[i+1][j], dp[i+1][j+1])
	return dp[0][0]