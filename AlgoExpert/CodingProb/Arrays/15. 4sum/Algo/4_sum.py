# Time = O(n^3)
# space = O(n^2)
def fourNumberSum(array, targetSum):
    cache = {}
	res = []
	
	for i in range(1, len(array)-1):
		for j in range(i+1 , len(array)):
			currentSum = array[i] + array[j]
			diff = targetSum - currentSum
			
			if diff in cache:
				for pair in cache[diff]:
					res.append(pair + [array[i], array[j]])
					
		for k in range(0,i):
			currentSum = array[k] + array[i]
			
			if currentSum not in cache:
				cache[currentSum] = [[array[k] , array[i]]]
			else:
				cache[currentSum].append([array[k] , array[i]])
				
	return res
