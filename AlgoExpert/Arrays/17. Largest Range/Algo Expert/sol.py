# Time = O(n)
# Space = O(n)
# Longest Consequtive Subsequence question leetcode

def largestRange(array):
    longest_range = 0
	nums_set = set(array)
	op = [0,0]

	for num in array:
		# Check if it is the beginning of the range
		if num - 1 not in nums_set:
			start_range = end_range = num
			cur_range_len = 1

			# look for next consecutive number
			while end_range + 1 in nums_set:
				end_range = end_range + 1
				cur_range_len += 1

			if cur_range_len > longest_range:
				longest_range = cur_range_len
				op[0] = start_range
				op[1] = end_range
	
	
	return op