# Time = O(n * k) # no is the height on stairs and k is the max steps
# Space = O(n)

def staircaseTraversal(height, maxSteps):
    # ways_to_top = [0 * (height + 1)] this wont work
	ways_to_top = [0 for _ in range(height + 1)]
	
	ways_to_top[0] = 1
	ways_to_top[1] = 1
	
	for cur_height in range(2, height + 1):
		step = 1
		
		while step <= maxSteps and step <= cur_height:
			ways_to_top[cur_height] += ways_to_top[cur_height - step]
			step +=1
			
	return ways_to_top[height]