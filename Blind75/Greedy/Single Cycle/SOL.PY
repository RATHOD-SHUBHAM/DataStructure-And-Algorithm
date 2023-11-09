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