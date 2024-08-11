# ------------------------ Copy ------------------------


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)

        k = k % n

        if k == 0:
            return nums

        nums[ : ] = nums[-k : ] + nums[ : -k]

        return nums
    

# ------------------------ Reverse ------------------------

'''
    Let n=7 and k=3.

    Original List                   : 1 2 3 4 5 6 7
    After reversing all numbers     : 7 6 5 4 3 2 1
    After reversing first k numbers : 5 6 7 4 3 2 1
    After revering last n-k numbers : 5 6 7 1 2 3 4 --> Result
'''

# Tc : O(n) | Sc : O(1)

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)

        k = k % n

        if k == 0:
            return nums

        self.reverse(0 , n - 1, nums)
        self.reverse(0 , k - 1 , nums)
        self.reverse(k, n -1 , nums)

    def reverse(self, left, right, nums):

        while left < right:
            nums[left] , nums[right] = nums[right], nums[left]

            left += 1
            right -= 1  