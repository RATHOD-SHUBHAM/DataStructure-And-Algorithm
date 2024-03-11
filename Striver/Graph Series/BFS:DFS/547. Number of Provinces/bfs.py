# BFS
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)

        visited = [False] * n

        queue = []

        no_of_province = 0

        for i in range(n):
            if visited[i] == True:
                continue
            
            queue.append(i)

            while queue:
                node = queue.pop(0)
                visited[node] = True

                for nei in range(len(isConnected[node])):
                    if isConnected[node][nei] == 0:
                        continue
                    
                    if visited[nei] == True:
                        continue
                    
                    queue.append(nei)
            
            no_of_province += 1
        
        return no_of_province