# Brute Force
# Sorting
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort() # n log n
        
        counter = collections.Counter(nums) # O(n)
        
        # print(counter[0])
        
        zero = nums[:counter[0]] # extra array = space O(n)
        
        nums = nums[counter[0]:]
        
        for i in zero:
            nums.append(i)
        
        print(nums)