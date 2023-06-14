# Tc and Sc: O(V*E) -> O(m * n)

# Based on the constrain, we know that min distance can lie in btn 0 - 10^6
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])
        
        directions = [ (0,-1), (0,1), (-1, 0), (1, 0)]
        
        # based on the constrains
        left = 0
        right = 1000000
        
        
        while left < right:
            
            # get the threshold
            mid = left + (right - left) // 2 # current threshold

            
            # this should reset every time we start from source cell
            visited = [[False for _ in range(n)] for _ in range(m)]
            
            # check if we can reach destination with the current threshold
            if self.canReach(0 , 0 , mid , visited, directions, m , n ,heights):
                # if we can reach - reduce threshold and check
                right = mid
            else:
                # with the current threshold we cant reach - so check for the remaining part
                left = mid + 1

        
        return right # or left
    
    def canReach(self, row , col , threshold , visited, directions, m, n, heights):
        # base
        if row == m - 1 and col == n - 1:
            # reached destination
            return True
        
        visited[row][col] = True
        
        for direction in directions:
            adj_row , adj_col = direction
            
            nei_row = adj_row + row
            nei_col = adj_col + col
            
            if nei_row < 0 or nei_row >= m or nei_col < 0 or nei_col >= n or visited[nei_row][nei_col] == True:
                continue
                
            cur_threshold = abs(heights[row][col] - heights[nei_row][nei_col])
            
            # current threshold should not exceed the actual threshold set
            if cur_threshold <= threshold:
                
                if self.canReach(nei_row , nei_col , threshold , visited, directions, m , n ,heights):
                    return True
                
        return False