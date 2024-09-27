class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = [[]]
        n = len(nums)
        
        for i in range(n):
            m = len(subset)
            # print("len: ", m)
            for j in range(m):
                cur_set = subset[j] + [nums[i]]
                # print(cur_set)
                subset.append(cur_set)
        
        return subset
    

# ---------------------------  BackTracking  ---------------------------

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
        