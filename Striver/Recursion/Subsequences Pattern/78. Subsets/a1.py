'''
https://stackoverflow.com/questions/72904209/why-do-we-need-to-copy-array-element-inside-backtracking

Why do we need to copy array element inside backtracking?
The reason is that, when you append nums to results, nums can still be changed even if it's inside results. Therefore the elements inside results will be changed everytime you change the original nums (in fact in the result all the values are identical). If you create a copy for each element you put in results, instead, the elements will all have different values.
'''


class Solution:
    def __init__(self):
        self.result = []

    def subsets(self, nums: List[int]) -> List[List[int]]:
        st = []

        def dfs(i):
            # base case
            if i >= len(nums):
                self.result.append(st.copy()) # self.result.append(st.[::]) this does same stuff
                return
            
            # Append the number
            st.append(nums[i])
            dfs(i + 1) # increase the index

            # Dont add the number
            st.pop()
            dfs(i + 1)

            return
        
        # Main -----
        dfs(0)
        return self.result
        

# --------------------------------------------------------------------
    
# Local Function
    
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