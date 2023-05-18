class Solution:
    def topoSort(self, graph):
        n = len(graph)

        stack = []
        visited = [False] * n

        for i in range(n):
            if not visited[i]:
                self.dfs(i, visited, stack, graph)
        
        return stack[::-1]

    def dfs(self, i, visited, stack, graph):
        if visited[i]:
            return
        
        visited[i] = True

        for nei in graph[i]:
            self.dfs(nei, visited, stack, graph)
        
        stack.append(i)

        return



if __name__ == '__main__':
    ip = [[], [], [3], [1], [0,1], [0,2]]
    obj = Solution()
    print(obj.topoSort(ip))
