# Time Complexity = O(n)
# Sapce Complexity = O(1)

def isValidSubsequence(array, sequence):
    top = 0
	down = 0
	
	while top < len(array) and down < len(sequence):
		if array[top] == sequence[down]:
			down += 1
		top += 1
		
	return True if down == len(sequence) else False