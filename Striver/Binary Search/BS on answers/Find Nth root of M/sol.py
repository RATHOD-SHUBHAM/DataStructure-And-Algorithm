class Solution:
    def NthRoot(self, n, m):
        left = 1
        right = m

        while left <= right:
            mid = left + (right - left) // 2
            
            sqr_val = 1
            for _ in range(n):
                sqr_val *= mid
            
            
            if sqr_val == m:
                return mid
                
            elif sqr_val < m:
                left = mid + 1
            
            else:
                right = mid - 1

        return -1