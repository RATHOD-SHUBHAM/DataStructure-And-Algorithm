# time = O(2 ^ (m + n))
# Space = O(m + n)

# brute force
def numberOfWaysToTraverseGraph(width, height):
    if width == 1 or height == 1:
		return 1
	return numberOfWaysToTraverseGraph(width-1, height) + numberOfWaysToTraverseGraph(width, height-1)
