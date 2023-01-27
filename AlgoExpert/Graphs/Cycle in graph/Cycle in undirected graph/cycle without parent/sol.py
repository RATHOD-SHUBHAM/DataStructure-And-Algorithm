# node cannot return from parent saying there is a cycle

class Solution:
    # return True or False if there is a cycle
    def cycleInGraph(self, edges):
        no_of_nodes = len(edges)

        # check if the nodes have been previously visited
        visited = [ False ] * no_of_nodes

        for node in range(no_of_nodes):

            # if a node is visted -  then all its node would have been explored
            # so no need to visit again.
            if visited[node]:
                continue

            # consider each initial node to not have any  parent as this is a graph node
            parent = -1
            cycle = self.detectCycle(node, edges, parent, visited)

            if cycle:
                return True
        
        return False

    def detectCycle(self, node, edges, parent, visited):
        # mark the node as visited
        visited[node] = True

        for child in edges[node]:
            # if the child is not visited - explore child
            if not  visited[child]:
                cycle = self.detectCycle(child, edges, node, visited)
                if cycle:
                    return True
            elif parent != node:
                return True

        return False




        

if __name__ == '__main__':
    edges = [
        [1],
        [2],
        [3],
        [],
    ]

    sol = Solution()
    cycle = sol.cycleInGraph(edges)

    if cycle:
        print("A cycle Detected")
    else:
        print(" No Cycle Found")


