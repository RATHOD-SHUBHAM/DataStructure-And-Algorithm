"""
[1, 2, 3]

Subsets
1. [1, 2, 3]
2. [1, 2]
3. [1, 3]
4. [1]
5. [2, 3]
6. [2]
7. [3]
8. []

"""

class Solution:
    def __init__(self):
        self.result = []

    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        def dfs(i , st):
            if i == n:
                self.result.append(st[::])
                return
            
            # Include the current element
            st.append(nums[i])
            dfs(i+1, st)

            # Donot include the current element
            st.pop()
            dfs(i+1, st)

            return
        
        i = 0
        st = []
        dfs(i, st)

        return self.result