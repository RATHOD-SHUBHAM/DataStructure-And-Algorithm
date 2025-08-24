def hasSingleCycle(array):
    n = len(array)

    """
    If a single cycle exists: Starting from ANY index will give you the same result - visit all n nodes and return to start.
    """
    startNode = 0
    
    curNode = 0
    visited = set()

    while curNode not in visited:
        visited.add(curNode)
        curNode = getNextNode(array, curNode, n)
    
    # After visiting exactly n nodes, check if we're back at start
    # Also ensure we visited exactly n unique nodes
    return curNode == startNode and len(visited) == n

    
def getNextNode(array, i, n):
    nxtNode = array[i] + i 

    nxtNode = nxtNode % n

    return nxtNode

if __name__ == "__main__":
    array = [2, 3, 1, -4, -4, 2]
    print(hasSingleCycle(array))

    # Test case 2: Not a single cycle
    array2 = [1, 1, -1, -1]
    print(hasSingleCycle(array2))

    # Test case 3: Single element pointing to itself
    array3 = [1]
    print(hasSingleCycle(array3))

    # Test case 4: Early return to start
    array4 = [3, 1, 1, 1]
    print(hasSingleCycle(array4))