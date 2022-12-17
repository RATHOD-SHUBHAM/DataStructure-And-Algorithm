# Time = O(n)
# space = O(n)

# sliding window
# window size will be maxStep plus one : because we will add the value from next cell and remove a value from previous cell
# consider step 3:
# ill inclue value of step 2 and remove a value from step 0
def staircaseTraversal(height, maxSteps):
    no_of_ways = 0
	list_of_heights_and_their_ways = [1]
	
	
	for cur_height in range(1,height+1):
		# creating window of size maxStep + 1
		start_of_window = cur_height - maxSteps - 1
		end_of_window = cur_height - 1
	
		if start_of_window >= 0:
			no_of_ways -= list_of_heights_and_their_ways[start_of_window]
			
		no_of_ways += list_of_heights_and_their_ways[end_of_window]
		
		# add to the lsit
		list_of_heights_and_their_ways.append(no_of_ways)
		
	return list_of_heights_and_their_ways[height]