"""
The questions simply means find the nearest water body from land

So this will be like find the nearest x -> we transform this into expand from x
"""

# Tc and Sc: O(m*n)
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m = len(isWater)
        n = len(isWater[0])

        visited = [[False for _ in range(n)]for _ in range(m)]

        dist = [[math.inf for _ in range(n)] for _ in range(m)]

        queue = collections.deque()

        # Mark all the water body as visited and the height as 0
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    visited[i][j] = True
                    dist[i][j] = 0
                    queue.append((0, i, j))
        
        neighbors = [[0,1], [0,-1], [1,0], [-1,0]]
        while queue:
            dst, i, j = queue.popleft()

            for nei in neighbors:
                nei_i = i + nei[0]
                nei_j = j + nei[1]

                if nei_i < 0 or nei_j < 0 or nei_i >= m or nei_j >= n or visited[nei_i][nei_j] == True or isWater[nei_i][nei_j] == 1:
                    continue
                
                new_dst = 1 + dst
                dist[nei_i][nei_j] = new_dst

                visited[nei_i][nei_j] = True
                queue.append((new_dst, nei_i, nei_j))
        
        return dist
