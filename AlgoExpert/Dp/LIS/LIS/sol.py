# time = O(nlogn)
# space = O(n)

def longestIncreasingSubsequence(array):
    # holds the index of its previous number in the subsequence
	subsequence_idx = [None for _ in array]
	
	# builds the subsequence on the go
	build_subsequence = [None for _ in range(len(array) + 1 )]
	
	# cur len of subsequence
	cur_len_of_subsequence = 0
	
	#go through the array and build subsequence
	for idx, num in enumerate(array):
		# get the correct position of the number in cur subsequence
		# always start left at 1 because at idx 0 we will have None so that it becomes easy to make first number point to previous ele as None
		correct_pos_of_num = binary_search(1,cur_len_of_subsequence, num, array, build_subsequence)
		
		# place the num at correct place in subsequence
		build_subsequence[correct_pos_of_num] = idx
		
		# append its previous number idx
		subsequence_idx[idx] = build_subsequence[correct_pos_of_num - 1]
		
		
		# if a new number get added then max len will increase 
		cur_len_of_subsequence = max(cur_len_of_subsequence, correct_pos_of_num)
	
	return buildSubsequence(array, subsequence_idx, build_subsequence[cur_len_of_subsequence])


def binary_search(left , right, num, array, build_subsequence):
	while left <= right:
		mid = left + (right - left) // 2
		
		# if my num is greater than number at mid. 
		# then the correct position of num is after middle number
		if num > array[build_subsequence[mid]]:
			left = mid + 1
		else:
			right = mid - 1
			
	return left

def buildSubsequence(array, subsequence_idx, cur_idx):
	subsequence = []
	
	while cur_idx is not None:
		subsequence.append(array[cur_idx])
		cur_idx = subsequence_idx[cur_idx]
		
	return list(reversed(subsequence))
