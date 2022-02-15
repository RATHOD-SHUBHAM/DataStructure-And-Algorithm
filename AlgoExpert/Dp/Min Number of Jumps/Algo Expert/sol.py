# same as leetcode
# Time and Space = O(n) | O(1)

def minNumberOfJumps(array):
    jump_count = 0
	
	left = 0 # next element
	right = 0 # farthest jump
	
	while right < len(array) - 1:
		farthest_jump = 0
		
		# count farthest jump for each element
		for i in range(left , right + 1):
			farthest_jump = max(farthest_jump , i + array[i])
			
			
		jump_count += 1
		
		# create next window
		left = right + 1
		right = farthest_jump
		
	return jump_count
