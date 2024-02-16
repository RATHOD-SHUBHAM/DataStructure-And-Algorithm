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


# ----------------------------------------------------------------

# Local Function

class Solution:
    def __init__(self):
        self.result = []

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        st = []
        curSum = 0
        i = 0
        self.backTracking(i, curSum, st, candidates, target)

        return self.result
    
    def backTracking(self, i, curSum, st, candidates, target):
        # basecase
        if curSum == target:
            self.result.append(st.copy())
            return
        
        if i >= len(candidates) or curSum > target:
            return
        
        # Include the current element
        st.append(candidates[i])
        curSum += candidates[i] # Since i have included current element, I need to increase the sum
        self.backTracking(i, curSum, st, candidates, target)

        # Not Include the current element
        st.pop()
        curSum -= candidates[i]
        self.backTracking(i + 1, curSum, st, candidates, target)

        return