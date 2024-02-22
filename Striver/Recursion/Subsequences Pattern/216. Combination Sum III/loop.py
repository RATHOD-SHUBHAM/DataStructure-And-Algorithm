# Solution 2: For Loop.

class Solution:
    def __init__(self):
        self.result = []
        self.end = 10

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        def backTrack(start, st, curSum):
            # basecase
            if len(st) == k and curSum == n:
                self.result.append(st.copy())
                return

            if start > 9 or len(st) > k or curSum > n:
                return
            
            for i in range(start, 10):
                st.append(i)
                curSum += i
                
                backTrack(i + 1, st, curSum)

                curSum -= i
                st.pop()

            return

        
        st = []
        i = 1
        curSum = 0
        backTrack(i, st, curSum)

        return self.result