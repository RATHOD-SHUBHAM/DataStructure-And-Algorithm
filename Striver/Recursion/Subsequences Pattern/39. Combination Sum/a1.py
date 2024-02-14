class Solution:
    def __init__(self):
        self.result = []

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def backTracking(i, curSum):
            # basecase
            if curSum == target:
                self.result.append(st[::])
                return
            
            if i >= len(candidates) or curSum > target:
                return
            
            # Append the current value
            st.append(candidates[i])
            curSum += candidates[i] # If i am including the current value, I also need to increase the sum
            backTracking(i, curSum)

            # Not to append the current value
            st.pop()
            curSum -= candidates[i] # If i am not including the current value then i need to decrese the sum i previously added
            backTracking(i + 1, curSum)

            return
        
        # Main Function
        st = []
        i = 0
        curSum = 0
        backTracking(i, curSum)

        return self.result


# ----------------------------------------------------------------------------------------
    
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