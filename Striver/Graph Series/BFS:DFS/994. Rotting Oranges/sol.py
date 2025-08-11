# Tc and Sc: O(m*n)

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        queue = collections.deque()
        
        # Step 1: Initial grid scanning to find fresh/rotten oranges
        no_of_fresh_orange = 0 # Instead of reiterating the grid, this counter will help us keep track of fresh orange in the end

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    no_of_fresh_orange += 1
                elif grid[i][j] == 2:
                    queue.append((i,j,0)) # coords and time
        # print(queue)
        # print(no_of_fresh_orange)

        # Step 2: Multi-source BFS simulation
        directions = [[0, 1], [0, -1],[1, 0],[-1, 0]]

        min_time = 0

        while queue:
            z = len(queue) # All oranges that get rotten in the same minute are processed together.

            for _ in range(z):
                i, j , tme = queue.popleft()
                min_time = tme

                # Explore its neighbors
                for nei in directions:
                    nei_i = i + nei[0]
                    nei_j = j + nei[1]

                    # If empty or already rotten, then skip
                    if nei_i < 0 or nei_j < 0 or nei_i >= m or nei_j >= n or grid[nei_i][nei_j] == 0 or grid[nei_i][nei_j] == 2:
                        continue
                    
                    # Fresh orange found -> rot it and reduce count of fresh orange
                    queue.append((nei_i, nei_j , tme + 1))
                    grid[nei_i][nei_j] = 2

                    no_of_fresh_orange -= 1
        
        # print(no_of_fresh_orange)

        return min_time if no_of_fresh_orange == 0 else -1
