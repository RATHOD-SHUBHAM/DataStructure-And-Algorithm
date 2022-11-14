# Time and Space Complexity: O(n) and O(1)

def longestPeak(array):
    longest_peak = 0
	cur_idx = 1 # we need left and right side of a mountain. 
	# so start from 1 and stop at last but 1.
	
	while cur_idx < len(array) - 1:
		#Treak every point as peak and check if this a peak.
		isPeak = array[cur_idx - 1] < array[cur_idx] and array[cur_idx + 1] < array[cur_idx]
		
		if not isPeak:
			cur_idx += 1
			continue
		
		# left_idx = cur_idx - 2 because. We already check the previous value while checking peak
		left_idx = cur_idx - 2
		
		while left_idx >= 0 and array[left_idx] < array[left_idx + 1]:
			left_idx -= 1
			
		right_idx = cur_idx + 2
		while right_idx < len(array) and array[right_idx] < array[right_idx - 1]:
			right_idx += 1
			
		
		cur_peak_len = (right_idx - 1) - (left_idx + 1) + 1 # +1 because of index error
		
		longest_peak = max(longest_peak , cur_peak_len)
		
		cur_idx += 1
		
	return longest_peak