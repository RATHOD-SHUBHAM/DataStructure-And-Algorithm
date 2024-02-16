class Solution:
    def __init__(self):
        self.result = []

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        st = []
        
        def backTrack(i, curSum):
            if i >= len(candidates) or curSum > target:
                return
            
            if curSum == target:
                self.result.append(st.copy())
                return

            st.append(candidates[i])
            curSum += candidates[i]
            backTrack(i, curSum) # May contain duplicate

            st.pop()
            curSum -= candidates[i]
            backTrack(i+1, curSum)

            return
        

        i = 0
        curSum = 0
        backTrack(i, curSum)

        return self.result