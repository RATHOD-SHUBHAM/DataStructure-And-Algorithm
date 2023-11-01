'''
    Time Complexity : O(3^m⋅n)
    The total number of cells in the matrix is given by m⋅n. 
    For the backtracking, there are at most 4 possible directions to explore, 
    but further, the choices are reduced to 3 (since we won't go back to where we come from). 
    Thus, considering 3 possibilities for every cell in the matrix the time complexity would be O(3^m⋅n) 

    The time complexity is exponential, hence this approach is exhaustive and results in Time Limit Exceeded (TLE).

'''

# ------------------------------------------------------------------------

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])

        self.minimum_effort = math.inf

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]


        # Helper Function ------------------------------------------------------

        def backTrack_dfs(row, col, max_difference):
            # check if we have reached the destination cell
            if row == m - 1 and col == n - 1:
                # capture the minimum effort to reach the destination
                self.minimum_effort = min(self.minimum_effort, max_difference)
                '''
                    minimum route effort = min(route effort) = min(maximum absolute difference)
                '''
                return max_difference


            # mark the cell in current route - mark the cells by making them as 0
            current_height = heights[row][col]
            heights[row][col] = 0 # marking

            min_effort = math.inf

            for direction in directions:
                adj_row , adj_col = direction

                nei_row = adj_row + row
                nei_col = adj_col + col

                if nei_row < 0 or nei_row >= m or nei_col < 0 or nei_col >= n or heights[nei_row][nei_col] == 0:
                    continue
                
                # difference between the cell
                nei_cell_height = heights[nei_row][nei_col]
                current_difference  = abs(current_height - nei_cell_height)

                # Check if this is the maximum different in the current route
                max_cur_difference = max(max_difference, current_difference) # dont alter the max_difference as it will further check the neighbors

                '''
                    If we have previously reached the destination, and have some difference X
                    if the new path effort is more than the previous difference X - then we dont have 
                    to move forward in this path

                    if the new path effort is less than the previous difference X - only then we 
                    move forward in this path
                '''

                if max_cur_difference < self.minimum_effort:
                    backTrack_dfs(nei_row, nei_col, max_cur_difference)
                    
                
            # Backtrack
            # unmark the current cell
            heights[row][col] = current_height
             
        
        
        # Function Call ------------------------------------------------------

        # row, col, maximum absolute difference
        backTrack_dfs(0,0,0) 
        return self.minimum_effort








# ------------------------------------------------------------------------

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])

        self.minimum_effort = math.inf

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]


        # Helper Function ------------------------------------------------------

        def backTrack_dfs(row, col, max_difference):
            # check if we have reached the destination cell
            if row == m - 1 and col == n - 1:
                # capture the minimum effort to reach the destination
                self.minimum_effort = min(self.minimum_effort, max_difference)
                '''
                    minimum route effort = min(route effort) = min(maximum absolute difference)
                '''
                return max_difference


            # mark the cell in current route - mark the cells by making them as 0
            current_height = heights[row][col]
            heights[row][col] = 0 # marking

            min_effort = math.inf

            for direction in directions:
                adj_row , adj_col = direction

                nei_row = adj_row + row
                nei_col = adj_col + col

                if nei_row < 0 or nei_row >= m or nei_col < 0 or nei_col >= n or heights[nei_row][nei_col] == 0:
                    continue
                
                # difference between the cell
                nei_cell_height = heights[nei_row][nei_col]
                current_difference  = abs(current_height - nei_cell_height)

                # Check if this is the maximum different in the current route
                max_cur_difference = max(max_difference, current_difference) # dont alter the max_difference as it will further check the neighbors

                '''
                    If we have previously reached the destination, and have some difference X
                    if the new path effort is more than the previous difference X - then we dont have 
                    to move forward in this path

                    if the new path effort is less than the previous difference X - only then we 
                    move forward in this path
                '''

                if max_cur_difference < self.minimum_effort:
                    previous_effort = backTrack_dfs(nei_row, nei_col, max_cur_difference)
                    
                    min_effort = min(min_effort, previous_effort)
                
            # Backtrack
            # unmark the current cell
            heights[row][col] = current_height
            return min_effort
             
        
        
        # Function Call ------------------------------------------------------

        # row, col, maximum absolute difference
        return backTrack_dfs(0,0,0) 
    

# ------------------------------------------------------------------------

# Different Function

class Solution:
    def __init__(self):
        self.minimum_effort = math.inf

    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        # row, col, maximum absolute difference
        return self.backTrack_dfs(0,0,0, directions, m, n, heights)

    def backTrack_dfs(self, row, col, max_difference,  directions, m, n, heights):
        # check if we have reached the destination cell
        if row == m - 1 and col == n - 1:
            # capture the minimum effort to reach the destination
            self.minimum_effort = min(self.minimum_effort, max_difference)
            '''
                minimum route effort = min(route effort) = min(maximum absolute difference)
            '''
            return max_difference


        # mark the cell in current route - mark the cells by making them as 0
        current_height = heights[row][col]
        heights[row][col] = 0 # marking

        min_effort = math.inf

        for direction in directions:
            adj_row , adj_col = direction

            nei_row = adj_row + row
            nei_col = adj_col + col

            if nei_row < 0 or nei_row >= m or nei_col < 0 or nei_col >= n or heights[nei_row][nei_col] == 0:
                continue
            
            # difference between the cell
            nei_cell_height = heights[nei_row][nei_col]
            current_difference  = abs(current_height - nei_cell_height)

            # Check if this is the maximum different in the current route
            max_cur_difference = max(max_difference, current_difference) # dont alter the max_difference as it will further check the neighbors

            '''
                If we have previously reached the destination, and have some difference X
                if the new path effort is more than the previous difference X - then we dont have 
                to move forward in this path

                if the new path effort is less than the previous difference X - only then we 
                move forward in this path
            '''

            if max_cur_difference < self.minimum_effort:
                previous_effort = self.backTrack_dfs(nei_row, nei_col, max_cur_difference, directions, m, n, heights)
                min_effort = min(min_effort, previous_effort)
            
        # Backtrack
        # unmark the current cell
        heights[row][col] = current_height
        return min_effort