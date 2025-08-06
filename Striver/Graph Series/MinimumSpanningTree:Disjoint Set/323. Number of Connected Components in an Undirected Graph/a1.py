# Tc and Sc : O(n + e), where n is the number of nodes and e is the number of edges

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = [False] * (n)

        # Get neighbor: Adjacency list ------------------------
        dic = collections.defaultdict(list)

        for edge in edges:
            u , v = edge
            
            dic[u].append(v)
            dic[v].append(u)


        # Helper Code: Traverse Connected Component ------------------------
        def dfs(node):
            if visited[node] == True:
                return
            
            visited[node] = True

            for child in dic[node]:
                if visited[child] == False:
                    dfs(child)
            
            return

        # Main Code ------------------------
        connectedComponents = 0

        # Traverse across all the node
        for node in range(n):
            # if the node has neighbors -> travers the path
            if node in dic:
                if visited[node] == False:
                    dfs(node)
                    connectedComponents += 1
            else:
                # This is a single node with no neighbor
                connectedComponents += 1
        
        return connectedComponents
