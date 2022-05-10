## least best approach

# Time = O(K ^ n) # no is the height on stairs and k is the max steps
# Space = O(n)

def staircaseTraversal(height, maxSteps):
    return helper(height,maxSteps)

def helper(height ,maxSteps):
	if height <= 1:
		return 1

	no_of_ways = 0

	for step in range(1,min(height, maxSteps)+1):
		no_of_ways += helper((height - step) , maxSteps)

	return no_of_ways