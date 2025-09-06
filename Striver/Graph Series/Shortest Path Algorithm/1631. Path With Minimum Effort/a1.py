# Backtracking : Time Limit Exceeded

class Solution:
    def __init__(self):
        self.minimum_effort = math.inf

    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        # row, col, maximum absolute difference
        self.backTrack_dfs(0,0,0, directions, m, n, heights)
        return self.minimum_effort

    def backTrack_dfs(self, row, col, max_difference,  directions, m, n, heights):
        # check if we have reached the destination cell
        if row == m - 1 and col == n - 1:
            # capture the minimum effort to reach the destination
            self.minimum_effort = min(self.minimum_effort, max_difference)
            '''
                minimum route effort = min(route effort) = min(maximum absolute difference)
            '''
            return


        # mark the cell in current route - mark the cells by making them as 0
        current_height = heights[row][col]
        heights[row][col] = 0 # marking

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
            # dont alter/mutate the max_difference as it will further check the neighbors
            max_cur_difference = max(max_difference, current_difference) 

            '''
                If we have previously reached the destination, and have some difference X
                if the new path effort is more than the previous difference X - then we dont have 
                to move forward in this path

                if the new path effort is less than the previous difference X - only then we 
                move forward in this path
            '''

            if max_cur_difference < self.minimum_effort:
                self.backTrack_dfs(nei_row, nei_col, max_cur_difference, directions, m, n, heights)
               
            
        # Backtrack
        # unmark the current cell
        heights[row][col] = current_height
        return
# ------------------------------------------------------------------------

# Dijkstras

# Calculate the minimum effort required for each cell and slowly move toward destination

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])

        # store the minimum effort of all cell
        min_effort = [[math.inf] * n for _ in range(m)]
        min_effort[0][0] = 0


        '''
        Logic:
            Heap will store the paths max effort to reach the cell
            And will pop out  minimum effort first
        '''
        minHeap = []
        heapq.heapify(minHeap)

        # path effort, row, col
        heapq.heappush(minHeap, (0,0,0))

        directions =  [(0,-1), (0,1), (-1, 0), (1, 0)]


        while minHeap:
            max_path_effort, row, col = heapq.heappop(minHeap)

            if row == m - 1 and col == n - 1:
                return max_path_effort # this will be the minimum effort to reach the destination
            
            cur_height = heights[row][col]

            for direction in directions:
                adj_row , adj_col = direction

                nei_row = adj_row + row
                nei_col = adj_col + col

                if nei_row < 0 or nei_row >= m or nei_col < 0 or nei_col >= n:
                    continue
                

                nei_height = heights[nei_row][nei_col]
                cur_path_difference = abs(cur_height - nei_height)

                # maximum route effort
                max_route_effort  = max(max_path_effort , cur_path_difference)


                # check and update the min effort
                if max_route_effort < min_effort[nei_row][nei_col]:
                    min_effort[nei_row][nei_col] = max_route_effort
                    heapq.heappush(minHeap, (max_route_effort,nei_row, nei_col))


# ------------------------------------------------------------------------

# Kruskal Algorithm
'''
    Since we access the edges in increasing order of difference, 
    and the current edge connected the source and destination cell, 
    we are sure that the current difference is the maximum absolute difference in our path with minimum efforts.
'''

class Disjoint:
    def __init__(self, n):
        self.rank = [0] * (n + 1)
        self.parent = [i for i in range(n+1)]
    
    def findParent(self, x):
        if self.parent[x] != x:
            # Path comprehension
            self.parent[x] = self.findParent(self.parent[x])
        
        return self.parent[x]
    
    def union_rank(self, u, v):
        # step 1: Find the Ultimate parent
        pu = self.findParent(u)
        pv = self.findParent(v)

        # step 2: Get the rank of ultimate parent
        rank_pu = self.rank[pu]
        rank_pv = self.rank[pv]

        # step 3: Compare and join
        if rank_pu < rank_pv:
            self.parent[pu] = pv
        elif rank_pv < rank_pu:
            self.parent[pv] = pu
        else:
            self.parent[pu] = pv
            self.rank[pv] += 1



class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])

        if m == 1 and n == 1:
            return 0

        V = m * n
        disjoint_obj = Disjoint(V)

        edgeList = []

        # Building edge list
        for row in range(m):
            for col in range(n):
                cell_no = row * n + col

                # Look up
                if row > 0:
                    diff = abs(heights[row - 1][col] - heights[row][col])

                    nei_cell_no = (row - 1) * n + col

                    edgeList.append([diff, nei_cell_no, cell_no])
                
                # Look Left
                if col > 0:
                    diff = abs(heights[row][col - 1] - heights[row][col])

                    nei_cell_no = row * n + (col - 1)

                    edgeList.append([diff, nei_cell_no, cell_no])

        
        # maximum absolute difference in increasing order
        edgeList.sort(key = lambda x : x[0])
        print(edgeList)


        for diff , u, v in edgeList:
            disjoint_obj.union_rank(u,v)

            if disjoint_obj.findParent(0) == disjoint_obj.findParent(row * n + col):
                return diff
            # if disjoint_obj.findParent(0) == disjoint_obj.findParent((m-1) * n + (n-1)):
            #     return diff
        
        return -1
    

# ------------------------------------------------------------------------

# Binary Search

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