# Time and Space Complexity: O(n^2)

def threeNumberSum(array, targetSum):
	array.sort()
	res = []
	
	cur_sum = 0
	
	for i in range(len(array) - 2):
		less_val = i + 1
		more_val = len(array) - 1
		
		while less_val < more_val:
			cur_sum = array[i] + array[less_val] + array[more_val]
			
			if cur_sum == targetSum:
				res.append([array[i] , array[less_val] , array[more_val]])
				less_val += 1
				more_val -=1
				
			elif cur_sum < targetSum:
				less_val += 1
			else:
				more_val -= 1
				
				
	return res

	# Time = O(n), N is number of competition
# Space = O(t), t is the number of teams 

