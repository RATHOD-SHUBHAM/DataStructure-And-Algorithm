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
        
