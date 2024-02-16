class Solution:
    def __init__(self):
        self.result = []

    def subsets(self, nums: List[int]) -> List[List[int]]:
        st = []
        i = 0
        
        def backTrack(i):
            if i >= len(nums):
                self.result.append(st[::])
                return
            
            # Include the current number
            st.append(nums[i])
            backTrack(i+1)

            # Remove the current number
            st.pop()
            backTrack(i+1)

            return


        backTrack(i)
        return self.result
    
# ------------------------------------------------------------------------------------------------
    
# Local Func
    
class Solution:
    def __init__(self):
        self.result = []

    def subsets(self, nums: List[int]) -> List[List[int]]:
        st = []
        i = 0
        self.dfs(i, st, nums)

        return self.result
    
    def dfs(self, i , st, nums):
        # base case
        if i >= len(nums):
            self.result.append(st.copy())
            return
        
        # Include the value
        st.append(nums[i])
        self.dfs(i + 1, st, nums)
        
        # dont include the value
        st.pop()
        self.dfs(i + 1, st, nums)

        return