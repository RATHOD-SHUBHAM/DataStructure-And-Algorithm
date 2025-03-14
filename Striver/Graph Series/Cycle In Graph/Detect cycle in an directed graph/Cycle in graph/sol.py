# TC: O(V + E) | SC : O(V)
def cycleInGraph(edges):
    n = len(edges)

    visited = [False] * n
    # keep track of current nodes ancestor
    track_path = [False] * n

    for node in range(len(edges)):
        # check if the node has been explored before
        if visited[node]:
            continue

        cyclePresent = detectCycle(node, edges, visited,  track_path)

        if cyclePresent:
            return True

    return False
        

def detectCycle(node, edges, visited, track_path):
    # mark the node as visited
    visited[node] = True
    # Node is being explored in current path
    track_path[node] = True

    for child in edges[node]:
        # if child is not visited
        if not visited[child]:
            cyclePresent = detectCycle(child, edges, visited, track_path)

            if cyclePresent:
                return True
        # if child is visited - check if the child was vivisted in same path
        elif track_path[child]:
            return True

    # remove node from path
    track_path[node] = False
    return False