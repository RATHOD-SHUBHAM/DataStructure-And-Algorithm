# Time = O(n * k) # no is the height on stairs and k is the max steps
# Space = O(n)

def staircaseTraversal(height, maxSteps):
    return helper(height,maxSteps,{0:1,1:1})

def helper(height, maxSteps,memoize):
	if height in memoize:
		return memoize[height]
	
	no_of_ways = 0
	
	for step in range(1, min(height,maxSteps)+1):
		no_of_ways += helper((height - step), maxSteps, memoize)
		
	memoize[height] = no_of_ways
	
	return no_of_ways