# Basics: https://www.youtube.com/watch?v=75yC1vbS8S8&ab_channel=takeUforward

# Tc: O(n^3) | O(n^2)
# Bellman Ford Algorithm - Single Source Shortest Path
import math
def detectArbitrage(exchangeRates):
    # convert all the edges to negative log: either log10, log2 or loge
    logExchangeRates = convertToLog(exchangeRates)
    print(logExchangeRates)

    # bellman Ford algorithm - if we can find a cycle of vertices such that the sum of their weights if negative, then we can conclude there exists an opportunity for currency arbitrage. 
    return bellmanFord(logExchangeRates)

def convertToLog(matrix):
    row_len = len(matrix)
    col_len = len(matrix[0])

    logMatrix = [[None for _ in range(col_len)] for _ in range(row_len)]

    for i in range(row_len):
        for j in range(col_len):
            # convert each value to negative log
            negative_log = -math.log2(matrix[i][j])
            logMatrix[i][j] =  negative_log
    
    return logMatrix


def bellmanFord(graph):
    n = len(graph)

    # create a distance array
    distance = [math.inf] * n
    distance[0] = 0

    # relax the edges for n - 1 time
    for _ in range(n-1):

        # so if the value stops decresing in at some point return False
        if not relaxEdges(distance, graph):
            return False

    # at this point we found the shortest path and no further changes can be made
    # but if our value changes - then we have negative cycle
    return relaxEdges(distance, graph)

def relaxEdges(distance, graph):
    # u = node, v = child
    # dist[v] = dist[u] + weight of edge < dist[v]

    update = False # check if the value is changing

    for sourceIdx, edges in enumerate(graph):
        # print(" sourceIdx, edges : ", sourceIdx, edges)
        for destinationIdx, weight in enumerate(edges):
            # print(" destinationIdx, child : ", destinationIdx, weight)
            # u = node, v = child -- dist[u] + weight of edge < dist[v]
            if distance[sourceIdx] + weight < distance[destinationIdx]:
                update = True # the value
                distance[destinationIdx] = distance[sourceIdx] + weight
    
    print("distance: ", distance)
    return update
    