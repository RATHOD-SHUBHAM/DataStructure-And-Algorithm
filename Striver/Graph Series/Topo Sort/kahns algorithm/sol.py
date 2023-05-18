class Solution:
    def topoSort(self, graph):
        n = len(graph)

        indegree = [0] * n

        # get the indegree count of each node
        for i in range(n):
            for nei in graph[i]:
                indegree[nei] += 1
        
        # get the node whose indegree count is 0
        queue = []
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)

        # start reducing the indegree of nei node
        count = 0
        topo_sort = []
        while queue:
            node = queue.pop(0)

            # reduce the indegree of nei
            for nei in graph[node]:
                indegree[nei] -= 1

                # if the indegree becomes zero add to queue
                if indegree[nei] == 0:
                    queue.append(nei)

            
            # increment the count 
            count += 1

            topo_sort.append(node)

        if count != n:
            # there is a cycle
            return 0
        else:
            return topo_sort



if __name__ == '__main__':
    ip = [[], [], [3], [1], [0,1], [0,2]]
    obj = Solution()
    print(obj.topoSort(ip))
