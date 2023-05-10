# Tc: O(n^2) | Sc:O(n)

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        
        visited_city = [False] * n
        
        province = 0
        
        # Go as deep as possible and mark each node as visited. When the node cannot be reachede that is a start of new province
        for i in range(n):
            if visited_city[i] == True:
                continue
            
            province += 1
            
            self.dfs(i, n, visited_city, isConnected)
        
        return province
    
    def dfs(self, i, n, visited_city, isConnected):
        
        if visited_city[i] == True:
            return
        
        visited_city[i] = True
        
        for j in range(n):
            
            if isConnected[i][j] == 1:
                self.dfs(j, n, visited_city, isConnected)
        
        return