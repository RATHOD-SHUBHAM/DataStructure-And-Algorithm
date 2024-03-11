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

                if i == j:
                    continue
                
                if isConnected[i][j] == 1:
                    dfs(j)

            return


        # Main Function -------------------------------------------------
        
        count = 0
        
        for i in range(n):
            
            if visited[i] == True:
                continue

            for j in range(n):

                if i == j:
                    continue
                
                visited[i] = True
                
                if isConnected[i][j] == 1:
                    dfs(j)

            count += 1

        return count


# ------ Sol 2 ------------------------

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)

        visited = [False] * n

        no_of_province = 0

        def dfs(idx):
            
            visited[idx] = True

            for nei in range(len(isConnected[idx])):
                if isConnected[idx][nei] == 0:
                    continue
                
                if visited[nei] == True:
                    continue
                
                dfs(nei)
            
            return


        for i in range(n):
            if visited[i] == True:
                continue
            
            dfs(i)
            no_of_province += 1
        
        return no_of_province