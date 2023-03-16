# Time = O(n^3) 
# space = O(n^2)


import math
def palindromePartitioningMinCuts(string):
    dp = [[False for _ in range(len(string))] for _ in range(len(string))]
	
	# O(n^2) for 2 for loop  + isPalindrome = O(n) = O(n^3)
	for i in range(len(string)):
		for j in range(i,len(string)):
			# palindrome() = O(n) and slicing = O(n)
			dp[i][j] = isPalindrome(string[i : j+1])
	# print(dp)
	
	
	minCuts = [math.inf for _ in range(len(string))]
	
	for i in range(len(string)):
		if dp[0][i]:
			minCuts[i] = 0
		else:
			# previous slice
			minCuts[i] = minCuts[i-1] + 1
			# or if there is a palindorme
			for j in range(1,i):
				if dp[j][i] == True and minCuts[j-1] + 1 < minCuts[i]:
					minCuts[i] = minCuts[j-1] + 1
					
	return minCuts[-1]
	

def isPalindrome(string):
	left = 0
	right = len(string) - 1
	
	while left < right:
		if string[left] != string[right]:
			return False
		else:
			left += 1
			right -= 1
	return True
