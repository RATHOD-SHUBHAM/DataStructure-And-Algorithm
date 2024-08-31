# Tc: O(n^2) | Sc: O(1)

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)

        total = 0

        for i in range(n):
            for j in range(i, n):
                smallest = min(nums[i : j + 1])
                largest = max(nums[i : j + 1])
                total += (largest - smallest)
        
        return total






