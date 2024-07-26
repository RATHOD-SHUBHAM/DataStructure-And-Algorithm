class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)
        
        for idx in range(n):
            if s[idx] == goal[0]:
                dup_s = s[idx : ] + s[ : idx]
                if dup_s == goal:
                    return True
        
        return False
