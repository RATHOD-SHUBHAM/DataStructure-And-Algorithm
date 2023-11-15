# Tc: O(2n) | Sc: O(n)

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Place them at the right Index
        new_nums = [None] * n

        positive_Index = 0
        negative_Index = 1

        for i in range(n):
            if nums[i] > 0:
                new_nums[positive_Index] = nums[i]
                positive_Index += 2
            else:
                new_nums[negative_Index] = nums[i]
                negative_Index += 2
        
        return new_nums