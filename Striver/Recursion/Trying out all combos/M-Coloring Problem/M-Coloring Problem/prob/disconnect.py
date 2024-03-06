def buildGraph(edges):
    graph = {}
    
    for idx, neighbors in enumerate(edges):
        for nei in range(len(neighbors)):
            if neighbors[nei] == 1:
                if idx in graph:
                    graph[idx].append(nei)
                else:
                    graph[idx] = []
                    graph[idx].append(nei)
    
    return graph
            
def graphColoring(edges, m, n):
    
    # build graph
    # print(edges)
    graph = buildGraph(edges)
    # print(graph)
    
    node_color = [0] * n
    
    for node in range(n):
        if node_color[node] != 0:
            continue
        
        isValid = backTrack(node, node_color, graph, m, n)
        
    
    for i in node_color:
        if i == 0:
            return False
    return True

def backTrack(idx, node_color, graph, m, n):
    # basecase
    if idx == n:
        return True
    
    
    for color in range(1, m + 1):
        if isPossible(idx, color, node_color, graph):
            node_color[idx] = color
            
            isValid = backTrack(idx + 1, node_color, graph, m, n)
            
            if isValid:
                return True
            
            node_color[idx] = 0
    
    return False
    

def isPossible(idx, color, node_color, graph):
    if idx not in graph:
        return True
    
    for nei in graph[idx]:
        if node_color[nei] == color:
            return False
    
    return True