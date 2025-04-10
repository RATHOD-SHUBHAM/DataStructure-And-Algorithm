class Solution:
    def recursion(self, n, nums):
        if n < 0:
            return 0
        
        if n == 0:
            return nums[0]
        
        pick = nums[n] + self.recursion(n-2, nums) # Cannot moce to adjacent house
        not_pick = 0 + self.recursion(n-1, nums) # If we dont pick current house, we can move to adjacent house

        return max(pick, not_pick)

    def house_robber_1(self, nums: List[int]) -> int:
        n = len(nums)
        return self.recursion(n-1, nums)
    
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n < 2:
            return nums[0]

        num_1 = nums[0 : n-1]
        num_2 = nums[1: n]

        return max(self.house_robber_1(num_1), self.house_robber_1(num_2))
        