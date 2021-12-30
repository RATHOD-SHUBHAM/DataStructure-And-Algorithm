# Time = ( (2 ^ n) * n)
# Space = ( (2 ^ n) * n)

def powerset(array):
    subset = [[]]
	
    for i in array:
        for j in range(len(subset)):
            prevSet = subset[j]
            curset = prevSet + [i]
            subset.append(curset)
            
    return subset

