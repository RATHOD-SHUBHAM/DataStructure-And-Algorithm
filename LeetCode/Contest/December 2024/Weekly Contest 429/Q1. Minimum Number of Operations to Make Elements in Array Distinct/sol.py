class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

        count = 0

        while len(nums) > 0:
            # check if every element in the array is unique
            if len(set(nums)) == len(nums):
                break

            # If there are duplicate, then remove the number from front
            nums = nums[3 : ]
            count += 1

        return count