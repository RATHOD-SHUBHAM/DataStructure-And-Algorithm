def maxSumIncreasingSubsequence(array):
	sumAt = [0] * len(array)
	
	sumAt[0] = array[0]
	
    for i in range(1,len(array)):
		for j in range(i):
			if array[j] < array[i]:
				sumAt[i] = max(sumAt[i] , array[i]+sumAt[j])
	
	print(sumAt)
	return max(sumAt)