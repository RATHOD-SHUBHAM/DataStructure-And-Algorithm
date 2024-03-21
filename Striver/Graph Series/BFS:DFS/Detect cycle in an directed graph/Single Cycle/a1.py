# DFS solution
def hasSingleCycle(array):
    n = len(array)

    visited = [False] * n

    for idx in range(n):

        startIdx = idx # Consider this to be the start idx

        if dfs(startIdx, idx, visited, array, n) == True:
            return True

    return False

'''
If the idx is already visited then check:
    - If this is the start idx.
        - If this is the start idx then check all the nodes have been visited or not.
'''
def dfs(startIdx, idx, visited, array, n):
    # Basecase
    if visited[idx] == True:
        if idx == startIdx:
            # if all the nodes have not been visited
            if False in visited:
                return False
            else:
                return True
        else:
            # if this is not the start idx - return False
            return False

    visited[idx] = True
    value = array[idx]

    # Get the next idx value
    nxtIdx = (idx + value) % n

    if  dfs(startIdx, nxtIdx, visited, array, n) == True:
            return True
    else:
        # unmark the node as visted for next iteration.
        visited[idx] = False
        return False
        
# --------- Logical way ------------------------------------------

def hasSingleCycle(array):
    n = len(array)

    no_of_nodes_visited = 0
    total_no_of_nodes = n

    startNode = 0
    curNode = 0

    visited = [False] * n

    while no_of_nodes_visited < total_no_of_nodes:
        # base case
        # if before visiting all node we return to startNode. then return False
        if 0 < no_of_nodes_visited < total_no_of_nodes and curNode == startNode:
            return False

        if visited[curNode] == True:
            break

        visited[curNode] = True
        no_of_nodes_visited += 1
        
        curNode = getNext(curNode, array)

    return curNode == startNode

def getNext(node, array):
    nxtNode = (array[node] + node) % len(array)
    return nxtNode