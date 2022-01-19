# Time = O(n)
# Space = O(1)

'''
2 Base cases:
	1. When I have not visited every node in my array -- but i have return back to start idx
		no of visted nodes < len(array) and curNode != startNode
	2. When I have visited all the node -- but insted of returning to start idx. I start revisiting other nodes again
		no of visted nodes > len(array) and curNode != startNode
Only right condition will be:
no of visted nodes == len(array) and curNode == startNode
'''

def hasSingleCycle(array):
    no_of_visited_nodes = 0
    startIdx, curIdx =  0,0
	
	# once the no_of_visited_nodes == len(array) exit the loop
    while no_of_visited_nodes < len(array):
        # if i visited a node and got back before visiting all other node
        if no_of_visited_nodes > 0 and curIdx == startIdx:
            return False
        no_of_visited_nodes += 1
        curIdx = jump_to_idx(array,curIdx)

    # once the no_of_visited_nodes == len(array)
    return curIdx == startIdx

def jump_to_idx(array,curIdx):
    jump = array[curIdx]
    nxtIdx = (curIdx + jump) % len(array)
    return nxtIdx if nxtIdx >= 0 else nxtIdx + len(array)