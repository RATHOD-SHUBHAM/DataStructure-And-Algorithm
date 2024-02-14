class Solution:
    def __init__(self):
        self.result = []

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # This will handle duplicate values
        st = []
        i = 0
        self.backTracking(st, i, nums)

        return self.result
    
    def backTracking(self, st, i, nums):
        # base case
        if i >= len(nums):
            self.result.append(st[::])
            return
        
        # Append the current element
        st.append(nums[i])
        self.backTracking(st, i + 1, nums)

        # Dont include the current number
        st.pop()
        ## Check for duplicate values
        while i + 1 < len(nums) and nums[i] == nums[i+1] :
            i += 1
        
        self.backTracking(st, i + 1, nums)

        return 