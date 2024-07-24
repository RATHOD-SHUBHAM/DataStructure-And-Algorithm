# Just a few more check than basic to improve time.

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)
        g = len(goal)

        if n != g:
            return False

        for idx in range(n):
            if s[idx] == goal[0]:
                if idx + 1 == n or s[idx + 1] == goal[1]:
                    dup_s = s[idx : ] + s[ : idx]
                    if dup_s == goal:
                        return True
        
        return False
