# Tc: O(2n) | Sc: O(n)

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        positive = []
        negative = []

        # Store all the positive and negative number
        for i in range(n):
            if nums[i] > 0:
                positive.append(nums[i])
            else:
                negative.append(nums[i])
        

        # Place them at the right Index
        new_nums = [None] * n
        for i in range(len(positive)):
            new_nums[i * 2] = positive[i]
            new_nums[(i*2) + 1] = negative[i]
        
        return new_nums