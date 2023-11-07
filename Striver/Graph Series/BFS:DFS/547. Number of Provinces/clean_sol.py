class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)

        visited = [False] * n

        # Helper -----------------------------------------------

        def dfs(i):

            if visited[i] == True:
                return
            
            visited[i] = True
            
            for j in range(n):
                
                if isConnected[i][j] == 1:
                    dfs(j)

            return


        # Main Function -------------------------------------------------
        
        count = 0
        
        for i in range(n):

            if visited[i] == True:
                continue

            dfs(i)

            count += 1

        return count
