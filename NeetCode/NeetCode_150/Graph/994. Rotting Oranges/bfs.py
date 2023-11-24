# BFS matrix
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        # In order to know if there are any fresh oranges that cannot be rotten 
        # We can see how many fresh oranges were present in beginning to how how many fresh are left out.

        # initialize queue
        queue = deque()

        # [up, down, left, right]
        directions = [[-1,0], [1,0], [0,-1], [0,1]]
        
        
        # Count the number of fresh and add rotten orange to queue
        fresh_orange = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh_orange += 1         
                
                elif grid[i][j] == 2:
                    queue.append([i,j])   
                    
        
        # Counter to see at what time fresh orange become 0
        time = 0
        
        while queue and fresh_orange > 0:
            
            # Loop through all the element of that pareticular time stamp
            for _ in range(len(queue)):
                row, col = queue.popleft()
                
                for adj_row, adj_col in directions:
                    nei_row = adj_row + row
                    nei_col = adj_col + col
                    
                    if ( nei_row < 0 or nei_row >= m or nei_col < 0 or nei_col >= n 
                        or grid[nei_row][nei_col] != 1 ):
                        continue
                        
                    # else
                    grid[nei_row][nei_col] = 2
                    queue.append([nei_row,nei_col])
                    
                    fresh_orange -= 1
                    
            time += 1 # Increase time after all the oranges in the current time stamp has been rotten
                
        return time if fresh_orange == 0 else -1