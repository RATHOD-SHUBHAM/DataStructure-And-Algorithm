# https://www.geeksforgeeks.org/videos/problem-of-the-day-30112023-shortest-path-from-1-to-n/

# Reverse engineering
class Solution:
    def minimumStep (self, n):
        steps = 0
        
        while n > 1:
            # check if this is divisible by 3
            if n % 3 == 0:
                n = n // 3
            else:
                # else subtract 1
                n -= 1
            
            steps += 1
        
        return steps