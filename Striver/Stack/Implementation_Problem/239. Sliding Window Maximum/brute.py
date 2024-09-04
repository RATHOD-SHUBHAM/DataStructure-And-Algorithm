# Tc: O(n + k) | Sc: O(1)

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        if k >= n:
            return [ max(nums)   ]
        
        op = []

        for i in range(n - k + 1): # O(n)
            cur_max = max(nums[i : i + k]) # Tc: O(k)
            op.append(cur_max)

        return op