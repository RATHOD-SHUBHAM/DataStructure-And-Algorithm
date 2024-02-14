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