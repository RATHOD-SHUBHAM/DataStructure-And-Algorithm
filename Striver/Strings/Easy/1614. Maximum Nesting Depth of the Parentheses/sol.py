class Solution:
    def maxDepth(self, s: str) -> int:
        cur_count = max_count = 0

        for i in s:
            if i == ')':
                cur_count -= 1
            elif i == '(':
                cur_count += 1
                max_count = max(max_count, cur_count)
        
        return max_count
