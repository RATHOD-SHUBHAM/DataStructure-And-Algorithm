# Kahns algorithm
# Tc: O(v+e) | Sc: O(n)

def cycleInGraph(edges):
    n = len(edges)
    
    indegree = [0] * n

    # get the indegree of each edge
    for i in range(n):
        for nei in edges[i]:
            indegree[nei] += 1

    # get the node with indegree 0
    queue = []
    for i in range(n):
        if indegree[i] == 0:
            queue.append(i)

    # reduce the indegree
    count = 0
    topo_sort = []
    while queue:
        node = queue.pop(0)

        for nei in edges[node]:
            indegree[nei] -= 1

            if indegree[nei] == 0:
                queue.append(nei)

        count += 1
        topo_sort.append(node)

    if count != n:
        return True
    else:
        return False
