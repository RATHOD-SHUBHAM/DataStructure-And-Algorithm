'''
There are 2 Conditions:
    1. Each number in candidates may only be used once in the combination.
    2. Note: The solution set must not contain duplicate combinations.
'''
class Solution:
    def __init__(self):
        self.result = []

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort() # to avoid using the same number again
        print(candidates)

        def backTracking(i, st, curSum):
            # basecase
            if curSum == target:
                self.result.append(st[::])
                return
            
            if i >= len(candidates) or curSum > target:
                return
            
            # Include a number
            st.append(candidates[i])
            curSum += candidates[i]
            backTracking(i + 1, st, curSum)

            # Dont include current number
            st.pop()
            curSum -= candidates[i]
            
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            backTracking(i + 1, st, curSum)



        # Main Function ---------------
        st = []
        curSum = 0
        i = 0

        backTracking(i, st, curSum)
        return self.result
        