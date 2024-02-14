'''
Hint: Sort the array,
Sorting basically help us skip all the duplicate value
'''

class Solution:
    def __init__(self):
        self.result = []

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        def backtrack(i):
            # Base case
            if i >= len(nums):
                self.result.append(st.copy())
                return
            
            # Include current number
            st.append(nums[i])
            backtrack(i + 1)

            # Donot include current element
            st.pop()
            ## make sure that we dont include duplicate
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            
            backtrack(i + 1)

            return
        
        # Main func
        st = []
        backtrack(0)

        return self.result

# --------  ---------------------------------------- ------------------------
    
# Local Function

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