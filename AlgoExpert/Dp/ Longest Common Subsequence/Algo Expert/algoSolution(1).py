# same aa leetcode solution plus one extra bit

def longestCommonSubsequence(str1, str2):
	text1 = str1
	text2 = str2
	# creating a 2 * 2 matrix
	dp = [[0 for _ in range(len(text2)+1) ] for _ in range(len(text1)+1)]

	# bottom up approach
	for i in reversed(range(len(text1))):
		for j in reversed(range(len(text2))):
			# whenever there is a match it will be in diagonal
			# all the match will be stored in diagonal
			# so when there is a match increase the count of diagonal by one
			if text1[i] == text2[j]:
				dp[i][j] = 1 + dp[i+1][j+1]
			else: # take the max value and fill in the matrix, so that the answer will travel up
				dp[i][j] = max(dp[i+1][j] , dp[i][j+1])

	return buildSeq(dp,text2)

# here am just adding the subsequence
def buildSeq(dp,text):
	seq = []
	
	i = 0
	j = 0
	
	while i != len(dp)-1 and j != len(dp[0])-1:
		if dp[i][j] == dp[i+1][j]:
			i += 1
		elif dp[i][j] == dp[i][j+1]:
			j += 1
		else: # move diagonal when there is a match
			seq.append(text[j])
			i += 1
			j += 1
	return seq
