from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = [False] * n
        
        # Get neighbor ------------------------
        
        dic = defaultdict(list)
        for i in range(len(edges)):
            parent, child = edges[i]
            dic[parent].append(child)
            dic[child].append(parent)
        
        # Helper Code ------------------------
        
        def dfs(i):
            if visited[i] == True:
                return
            
            visited[i] = True
            
            # check if the node has any edge
            if i in dic:
                for child in dic[i]:
                    if visited[child] == False:
                        dfs(child)

            return
        
        
        # Main Code ------------------------
        
        connectedComponents = 0
        
        for i in range(n):
            # if there is a edge
            if i in dic:
                if visited[i] == False:
                    dfs(i)
                    connectedComponents += 1
                
            # if there is no edge - single node
            else:
                connectedComponents += 1
        
        return connectedComponents