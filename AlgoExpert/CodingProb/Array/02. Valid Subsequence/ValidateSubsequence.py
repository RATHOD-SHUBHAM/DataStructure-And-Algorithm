# time and Space = O(n) | O(1)


def isValidSubsequence(array, sequence):
	arrID, seqID = 0 , 0
	
	while arrID < len(array) and seqID < len(sequence):
		if array[arrID] == sequence[seqID]:
			seqID += 1
			
		arrID += 1
	
	# ill reach the end of sequence if all the element in the sequence has matched the array 
	return seqID == len(sequence)

