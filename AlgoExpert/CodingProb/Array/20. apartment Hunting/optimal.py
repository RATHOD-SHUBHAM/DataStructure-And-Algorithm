# Time and space = O(br)

def apartmentHunting(blocks, reqs):
    minDistanceOfReqFromEachBlock = []
	
	# for each block find its farthest requirement
	
	# for each block find min distance of particular req
	for i in range(len(reqs)):
		minDistanceOfReqFromEachBlock.append(getMinDistance(blocks, reqs[i]))
	# print(minDistanceOfReqFromEachBlock)
	
	# find the distance of max requirement
	maxDistanceOfReqFromEachBlock = getMaxDistanceAtBlocks(minDistanceOfReqFromEachBlock,blocks)
	# print(maxDistanceOfReqFromEachBlock)
	
	# get the block with min distance to other block with all req
	return getMinDistBlock(maxDistanceOfReqFromEachBlock)


def getMinDistance(blocks, req):
	minDist = [0 for _ in blocks]
	closestDist = float("inf")

	# closest req that appeared before the block
	for i in range(len(blocks)):
		if blocks[i][req]:
			closestDist = i
		# find the distance
		minDist[i] = distance(i, closestDist)
	
	# move in reverse order
	closestDist = float("inf")	
	# move in reverse order: closest requirement that appaeared after the block
	for i in reversed(range(len(blocks))):
		if blocks[i][req]:
			closestDist = i
		# find the distance
		dist = distance(i, closestDist)
		
		# find the min distance on left and right block
		minDist[i] = min(minDist[i] , dist )
	
	return minDist



def getMaxDistanceAtBlocks(minDistanceOfReqFromEachBlock,blocks):
	maxDist = [0] * len(blocks)
	
	for i in range(len(blocks)):
		dist = float("-inf")
		for j in range(len(minDistanceOfReqFromEachBlock)):
			dist = max(dist, minDistanceOfReqFromEachBlock[j][i])
		maxDist[i] = dist
	
	# print(maxDist)
	return maxDist
	
	
def distance(i, closestDist):
	return abs(i - closestDist)


def getMinDistBlock(maxDistanceOfReqFromEachBlock):
	minDist = float("inf")
	idx = 0
	
	for i in range(len(maxDistanceOfReqFromEachBlock)):
		cur_val = maxDistanceOfReqFromEachBlock[i]
		
		if cur_val < minDist:
			minDist = cur_val
			idx = i
			
	return idx