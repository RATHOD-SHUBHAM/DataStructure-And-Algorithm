class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 0
        
        # Build a dictionary to store the positions of each value in the array
        positions = {}
        for i in range(n):
            if arr[i] not in positions:
                positions[arr[i]] = []
            positions[arr[i]].append(i)
        
        # BFS algorithm to find the minimum number of jumps
        visited = set()
        q = [(0, 0)]  # (position, jumps)
        while q:
            pos, jumps = q.pop(0)
            
            # Check if we've reached the end of the array
            if pos == n - 1:
                return jumps
            
            # Jump to adjacent indices
            for next_pos in [pos-1, pos+1]:
                if 0 <= next_pos < n and next_pos not in visited:
                    visited.add(next_pos)
                    q.append((next_pos, jumps+1))
            
            # Jump to indices with the same value
            if arr[pos] in positions:
                
                for next_pos in positions[arr[pos]]:
                    if next_pos not in visited:
                        if next_pos == pos:
                            visited.add(next_pos)
                            continue
                        visited.add(next_pos)
                        q.append((next_pos, jumps+1))
                
                # We don't need to keep track of the positions as it might be a duplicate value
                del positions[arr[pos]]
        
        return -1  # It's not possible to reach the end of the array