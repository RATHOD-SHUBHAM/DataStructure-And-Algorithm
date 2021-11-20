# Brute Force or Naive Solution
# Time Complexity = O(n^2)
# Space Complexity = O(1)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False