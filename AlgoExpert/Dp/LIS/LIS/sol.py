# Time: O(nlogn)
# space = O(n)

def longestIncreasingSubsequence(array):
    sequences = [None for _ in range(len(array))]
	# index = we will add none : because while building ubsequence we stop when we reach none
	index = [None for _ in range(len(array) + 1 )]
	length = 0
	
	for idx, num in enumerate(array):
		left = binarySearch(1,length,num, array, index)
		# print("len is : ",left)
		sequences[idx] = index[left - 1]
		index[left] = idx 
		length = max(length , left)
	print(length)	
	return buildSequence(sequences,array,index[length])

# perform binary search
def binarySearch(left,right,num,array,index):
	while left <= right:
		mid = left + (right - left) // 2
		print("mid: ",mid)
		if array[index[mid]] < num:
			left = mid + 1
		else: 
			right = mid - 1
	return left

# build the subsequence
def buildSequence(sequence,array, curIdx):
	seq = []
	while curIdx is not None:
		seq.append(array[curIdx])
		curIdx = sequence[curIdx]
	return list(reversed(seq))