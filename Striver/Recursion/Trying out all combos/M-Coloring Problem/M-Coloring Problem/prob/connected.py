def buildGraph(edges):
    nei_graph = {}
    
    for idx, neighbors in enumerate(edges):
        for nei_idx in range(len(neighbors)):
            if neighbors[nei_idx] == 1:
                if idx in nei_graph:
                    nei_graph[idx].append(nei_idx)
                else:
                    nei_graph[idx] = []
                    nei_graph[idx].append(nei_idx)
                    
    # print(nei_graph)
    return nei_graph

def graphColoring(edges, m, n):
    
    # Build Graph with adjacent neighbor
    graph = buildGraph(edges)
    print(graph)
    
    # Start coloring the graph
    node_color = [0] * n # Keep track of color for every node
    
    idx = 0 # start index
    
    isValid = backTrack(idx, node_color, graph, m, n)
    
    if isValid:
        print('Solution Exist: With these colors:')
        print(node_color)
        return 1
    
    print('No solution exist')
    return 0

def backTrack(idx, node_color, graph, m, n):
    # base case
    if idx == n:
        return True
        
    # select color
    for color in range(1, m + 1):
        
        # check if it is possible to color the current node with the present color
        if isPossible(color, idx, node_color, graph):
            # add the current color to the node
            node_color[idx] = color
            
            isValid = backTrack(idx + 1, node_color, graph, m, n)
            if isValid:
                return True
            
            # change back the node color
            node_color[idx] = 0
        
    return False    

def isPossible(color, idx, node_color, graph):
    if idx not in graph:
        return True
    # compare the current color with neighbors
    for nei in graph[idx]:
        if node_color[nei] == color:
            return False
    
    return True


if __name__ == '__main__':
    # edges = [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]]
    # m = 3
    # n = 4 # len of edges

    # edges=[[0, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 1], [0, 0, 0, 0, 1], [1, 0, 1, 1, 0]]
    # m = 1
    # n = 5

    edges = [[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    m = 9
    n = len(edges) # 14

    # n = 4
    # edges = [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]]
    # m = 3

    canBuild = graphColoring(edges=edges,
                             m=m,
                             n=n
                             )
    
    print(canBuild)


