# Time = O(n)
# Space = O(1)

def hasSingleCycle(array):
    total_no_of_nodes = len(array) # total no of nodes
    no_of_visited_nodes = 0
    startIdx = 0
    curIdx =  0
	
	# make sure we have visited all the nodes
    while no_of_visited_nodes < total_no_of_nodes:
        # if we have visited some number of nodes 
        # and we got back to start node before traversing all the node, then return false
        # because only after travesing all the node we must return to start node
        if (no_of_visited_nodes > 0 
            and 
            no_of_visited_nodes < total_no_of_nodes 
            and 
            curIdx == startIdx):
            return False
            
        no_of_visited_nodes += 1
        curIdx = jump_to_idx(array,curIdx)

    # once we have traversed all the node, check if we came back to start node
    return curIdx == startIdx

def jump_to_idx(array,curIdx):
    jump = array[curIdx]

    # % len(array) - to get back to the start
    nxtIdx = (curIdx + jump) % len(array)
    return nxtIdx 
