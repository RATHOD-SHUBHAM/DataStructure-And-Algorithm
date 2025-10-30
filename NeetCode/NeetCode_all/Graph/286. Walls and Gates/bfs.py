class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m = len(rooms)
        n = len(rooms[0])

        visited = set()

        directions = [[-1,0], [1,0], [0,-1], [0,1]]

        queue = []
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append([i, j , 0]) # distance
        
        while queue:
            row, col, dist = queue.pop(0)

            for adj_row, adj_col in directions:
                nei_row = adj_row + row
                nei_col = adj_col + col

                # if the node has been previously visited means it will have the minimum distance
                if nei_row < 0 or nei_row >= m or nei_col < 0 or nei_col >= n or rooms[nei_row][nei_col] != 2147483647 or (nei_row, nei_col) in visited:
                    continue
                
                # this will make sure that we have minimum distance
                visited.add((nei_row, nei_col)) 

                rooms[nei_row][nei_col] = dist + 1 # Updated distance
                queue.append([nei_row, nei_col , rooms[nei_row][nei_col]]) 


        return rooms