class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        
        visited = [False] * n
        
        # Helper -------
        def dfs(i):
            
            if visited[i] == True:
                return
            
            visited[i] = True
            
            for j in range(n):
                if isConnected[i][j] == 1 and visited[j] == False:
                    dfs(j)
                    
            return
                    
        
        
        # Main --------
        
        province = 0
        
        for i in range(n):
            if visited[i] == False:
                dfs(i)
                province += 1
        
        return province