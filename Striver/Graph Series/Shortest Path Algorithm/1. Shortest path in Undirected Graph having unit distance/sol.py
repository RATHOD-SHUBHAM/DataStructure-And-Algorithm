import math
from collections import defaultdict

class Solution:
    def shortestPath(self, edges, n, m, src):
        
        # creating a graph
        neighbors = defaultdict(list)
        for i in range(len(edges)):
            parent, child = edges[i]
            
            neighbors[parent].append(child)
            neighbors[child].append(parent)
        
        # print(neighbors)
        
        # finding the distance
        distance = [math.inf] * n
        distance[src] = 0
        
        queue = []
        queue.append(src)
        
        while queue:
            node = queue.pop(0)
            
            for nei in neighbors[node]:
                # check if the node has not been previously visted
                # if it was previously visited then it would have already had the shortest path
                if distance[nei] == math.inf:
                    newDist = distance[node] + 1
                    distance[nei] = newDist
                
                    queue.append(nei)
        # print(distance)

        return -1 if math.inf in distance else distance

if __name__ == "__main__":
    n = 9 
    m = 10
    edges =[[0,1],[0,3],[3,4],[4 ,5],[5, 6],[1,2],[2,6],[6,7],[7,8],[6,8]]
    # edges =[[0,1],[0,3],[3,4],[4 ,5],[5, 6],[1,2],[2,6],[6,7]] 
    src = 0

    obj = Solution()
    print(obj.shortestPath(edges, n, m, src))