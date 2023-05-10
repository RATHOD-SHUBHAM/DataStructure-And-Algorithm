# BFS matrix
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # initialize queue
        q = deque()
        
        # In order to know if there are any fresh oranges that cannot be rotten 
        # We can see how many fresh oranges were present in beginning to how how many fresh are left out.
        # we can keep a counter for that
        
        time = fresh = 0
        
        
        # Count the number of fresh and rotten oranges
        Row = len(grid)
        Col = len(grid[0])
        
        for i in range(Row):
            for j in range(Col):
                if grid[i][j] == 1:
                    fresh += 1          # Number of fresh oranges initially
                elif grid[i][j] == 2:
                    q.append([i,j])     # Number of rotten oranges initially
                    
        
        
        # Inorder to move in 4 direction we need directions
        # [up, down, left, right]
        directions = [[-1,0], [1,0], [0,-1], [0,1]]
        
        # I need to return time
        # when all my oranges have become rotten or when there are no more fresh oranges remaining
        # when there are rotten oranges and when there are fresh oranges I need to keep rotting the other oranges
        while q and fresh > 0:
            for i in range(len(q)):
                r,c = q.popleft()
                
                # I move in all 4 directions to check if i can rot the oranges
                for dr,dc in directions:
                    row, col = dr + r, dc + c
                    
                    if (
                        ( row < 0 or row == len(grid) )  # if my row is in border and goes out of bounce
                        or 
                        ( col < 0 or col == len(grid[0]) )  # if my col is in border and goes out of bounce
                        or 
                        grid[row][col] != 1 # if my cell is already rotten or empty
                       ):
                        continue # do nothing --> move to other cell
                        
                    # else
                    grid[row][col] = 2
                    q.append([row,col])
                    fresh -= 1
                    
            time += 1 # for loop --> length of queue will only increase when I exit the for loop.
            # no matter I keep appending elements in the loop. until it wont exit for loop its len value wont increase
            # and we add time in the end becasue if there are two value in queue then both will start rotting other oranges at same time
            # So time will increase after the for loop has been complete
            
            
        return time if fresh == 0 else -1
    # return time all the oranges are rotten and this is know by our fresh counter
    # if any orange is left which cant be reached then we return -1