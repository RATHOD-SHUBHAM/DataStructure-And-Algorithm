# Tc :O( v + e) | O(e)

# Find a bridge in graph
def twoEdgeConnectedGraph(edges):
    if len(edges) == 0:
        return True # empty graph is two edged graph

    startNode = 0
    startNodeArrivalTime = 0
    parentNode = -1 # initial node will not have any parent

    # nodes arraival time
    arrivalTime = [-1] * len(edges) # chose any value less than start node arraival time

    
    # for a node get its ancestor arraival time
    bridgePresent = getMinimumArrivalTimeOfAncestor(startNode, parentNode, startNodeArrivalTime, arrivalTime, edges)

    if bridgePresent == -1:
        return False

    # we must have returned back to startNode after visiting all node
    return checkArrivalTime(arrivalTime)

def getMinimumArrivalTimeOfAncestor(curNode, parentNode, curNodeArrivalTime, arrivalTime, edges):
    arrivalTime[curNode] = curNodeArrivalTime

    # Before exploring the neighboring nodes - lets assume the min time to be same as arrivalTime
    minArrivalTime = curNodeArrivalTime

    for neighbor in edges[curNode]:
        # if the neighbor is not yet visited
        if arrivalTime[neighbor] == -1:
            neighborMinimumArrivalTimeOfAncestor = getMinimumArrivalTimeOfAncestor(neighbor, curNode, curNodeArrivalTime + 1, arrivalTime, edges)
            minArrivalTime = min(neighborMinimumArrivalTimeOfAncestor, minArrivalTime)
        # if the node is been visited before - then it must be a parent or ancestor
        # if parent -- skip
        elif neighbor != parentNode:
            ancestorArrivalTime = arrivalTime[neighbor]
            minArrivalTime = min(ancestorArrivalTime , minArrivalTime)

    # if bridge is detected
    if curNodeArrivalTime == minArrivalTime:
        # if the arrival time of a node matched with minArrivalTime - then only way to reach the child is via current Node
        # if the current node is not the start node - then we have a bridge
        if parentNode != -1:
            return -1

    return minArrivalTime

def checkArrivalTime(arrivalTime):
    for time in arrivalTime:
        if time == -1: # bridge is present - so graph is not 2 way connected
            return False
    return True