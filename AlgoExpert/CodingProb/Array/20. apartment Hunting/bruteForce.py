# brute force
# time = O(b^2 + r)
# space = O(b)
def apartmentHunting(blocks, reqs):
	maxDistAtBlock = [float("-inf") for _ in blocks]
	
	for i in range(len(blocks)):
		# for each block find the minimum distance to other requirements
		for req in reqs:
			closestReqDist = float("inf")
			for j in range(len(blocks)):
				# check if the req is present at current block
				if blocks[j][req]: # dict value
					reqFromThatPerticularBlock = distanceBetweenBlock(i ,j)
					closestReqDist = min(closestReqDist, reqFromThatPerticularBlock)
				
			# choose the farthest req
			maxDistAtBlock[i] = max(maxDistAtBlock[i], closestReqDist)
	
	# index with minimum value is closest block to most building
	return idxWithMinValue(maxDistAtBlock)

def idxWithMinValue(maxDistAtBlock):
	idx = 0
	minValue = float("inf")
	
	for i in range(len(maxDistAtBlock)):
		cur_val = maxDistAtBlock[i]
		
		if cur_val < minValue:
			minValue = cur_val
			idx = i
	return idx

	
	
def distanceBetweenBlock(i ,j):
	return abs(i - j)