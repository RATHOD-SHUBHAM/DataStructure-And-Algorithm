class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        
        if s[-1] != '0':
            return False
        
        visited = set()
        visited.add(0)
        queue = deque()
        queue.append(0)
        
        while queue:
            idx = queue.popleft()
            
            if idx == n - 1:
                return True
            
            for nxt_idx in range(idx + minJump , idx + maxJump + 1):
                if nxt_idx < n and nxt_idx not in visited and s[nxt_idx] == '0':
                    visited.add(nxt_idx)
                    queue.append(nxt_idx)
            
        return False