class Solution:
    def __init__(self):
        self.result = []

    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def backTrack(i, st):
            if i >= len(nums):
                self.result.append(st[::])
                return
            
            # Include the current number
            st.append(nums[i])
            backTrack(i + 1, st)

            # donot include the current number
            st.pop()
            backTrack(i + 1, st)
        
            return
        
        st = []
        i = 0
        backTrack(i, st)

        return self.result
        