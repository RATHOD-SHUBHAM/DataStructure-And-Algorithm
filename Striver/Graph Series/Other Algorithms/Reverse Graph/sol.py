from collections import defaultdict
def transposeGraph(adj, adj_transpose):
    for i in range(len(adj)):
        parent = i
        
        childrens = adj[i]
        
        for child in childrens:
            adj_transpose[child].append(parent)
    
    return

if __name__ == '__main__':
    adj = [[2, 3], [0], [1], [4], []]
    adj_transpose = defaultdict(list)
    transposeGraph(adj, adj_transpose)
    print(adj_transpose)

