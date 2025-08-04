"""
mutable object references.

If we dont create a copy, both will point to same objects memory
"""

# Tc and Sc: O(n)
import random

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.original = nums[:]

    def reset(self) -> List[int]:
        self.nums = self.original[:]
        return self.nums
        

    def shuffle(self) -> List[int]:
        # random.shuffle() shuffles the list in-place and returns None
        random.shuffle(self.nums) # O(n) space
        return self.nums
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

# ------------------  Optimal : Fisher Yates Algorithm ----------------------------------

# Tc: O(n)
# Sc: O(1)

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.original = nums[:]

    def reset(self) -> List[int]:
        self.nums = self.original[:]
        return self.nums
        

    def shuffle(self) -> List[int]:
        for i in reversed(range(len(self.nums))):
            j = random.randint(0, i)

            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]

        return self.nums
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()