# Tc: O(n) | Sc: O(1)

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        if n < 2:
            return nums

        # If k is larger than n, rotating by n brings array back to original,
        # so only the remainder k % n actually matters
        if k > n:
            k = k % n

        # 1. Reverse the entire array.
        self.swap(nums, 0, n-1)

        # 2. Reverse the first k elements.
        self.swap(nums, 0, k-1)

        # 3. Reverse the remaining (n-k) elements.
        self.swap(nums, k, n-1)

        return nums
    
    def swap(self, nums, i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        
        return

        