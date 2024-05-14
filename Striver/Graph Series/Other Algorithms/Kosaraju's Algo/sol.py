'''
Strongly Connected Components are only possible in Directed Graph.

Three Steps:
 1. Sort node based on their finish time.
 2. Reverse a graph.
 3. Perform DFS and check for individual components.
'''

from collections import defaultdict
class Solution:
    
    #Function to find number of strongly connected components in the graph.
    def kosaraju(self, V, adj):
        # Step 1 - Sort the nodes based on finish time
        stack = []
        visited = [False] * V
        for i in range(V):
            if visited[i] == False:
                self.finishTime(i, stack, visited, adj)
        
        # print(stack)
        
        # step 2: Reverse a graph
        adj_transpose = defaultdict(list)
        self.transposeGraph(adj, adj_transpose)
        # print(adj)
        # print(adj_transpose)
        
        # step 3: perform DFS
        count = 0
        visited = [False] * V
        SCC = []
        
        while stack:
            i = stack.pop()
            if visited[i] == False:
                scc = []
                self.dfs(i,visited, scc, adj_transpose)
                count += 1
                SCC.append(scc)
        
        # print(count)
        # print(SCC)
        
        return count
        # return len(SCC)
    
    # ---------------------------------------------------------------------------
    
    # Step 1 function - Sort the nodes based on finish time    
    def finishTime(self, i, stack, visited, adj):
        visited[i] = True
        
        for nei in adj[i]:
            if visited[nei] == False:
                self.finishTime(nei, stack, visited, adj)
        
        stack.append(i)
        
        return
    
    # step 2 function: Reverse a graph
    def transposeGraph(self, adj, adj_transpose):
        for i in range(len(adj)):
            parent = i
            
            childrens = adj[i]
            
            for child in childrens:
                adj_transpose[child].append(parent)
        
        return
            
    
    # step 3 function: perform DFS
    def dfs(self, i, visited, scc, adj_transpose):
        
        visited[i] = True
        
        for nei in adj_transpose[i]:
            if visited[nei] == False:
                self.dfs(nei,visited, scc, adj_transpose)
                
        scc.append(i)
        
        return