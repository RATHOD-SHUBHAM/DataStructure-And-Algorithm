# Time = Space = O( n*2^n )

def powerset(array):
    subset = [[]]
	
	for i in array:
		for j in range(len(subset)):
			prevSet = subset[j]
			curset = prevSet + [i] # [a] + [b] = [a,b]
			subset.append(curset)
			
	return subset