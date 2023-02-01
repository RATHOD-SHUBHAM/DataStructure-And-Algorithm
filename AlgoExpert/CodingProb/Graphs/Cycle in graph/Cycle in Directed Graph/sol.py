# TC: O(V + E) | SC : O(V)

def cycleInGraph(edges):
    n = len(edges)

    # keep track of visited node -- if the node is visited then there was no cycle found
    # if cycle was found then we would have returned True
    visited = [False] * n

    # keep track of current nodes ancestor
    ancestor = [False] * n

    # go through every node and check if there is a cycle
    for node in range(len(edges)):
        # check if the node has been explored before
        if visited[node]:
            continue

        cyclePresent = detectCycle(node, edges, visited, ancestor)

        if cyclePresent:
            return True

    return False
        

def detectCycle(node, edges, visited, ancestor):
    # mark the node as visited
    visited[node] = True

    # is ancestor for its children node
    ancestor[node] = True

    for child in edges[node]:
        # if child is not visited
        if not visited[child]:
            cyclePresent = detectCycle(child, edges, visited, ancestor)

            if cyclePresent:
                return True
        # if child is visited - check if the child is ancestor of current node
        elif ancestor[child]:
            return True

    # if there is no children or none of its children has cycle, remove the node as ancestor node
    ancestor[node] = False
    return False