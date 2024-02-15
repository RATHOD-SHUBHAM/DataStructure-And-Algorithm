class Solution:
    def __init__(self):
        self.result = []

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        def backTrack(i, curSum, st, count):
            # basecase

            # First time , i = 1 and we have [] empty list
            if i > 10 or count > k or curSum > n:
                return
            
            if count == k and curSum == n:
                self.result.append(st.copy())
                return

            if count == k and curSum != n:
                return

            # Include the current number
            st.append(i)
            curSum += i
            count += 1
            backTrack(i + 1, curSum , st, count)

            # Donot want to include the current number
            st.pop()
            curSum -= i
            count -= 1
            backTrack(i + 1, curSum , st, count)

            return 

        # Main function
        st = []
        curSum = 0
        count = 0
        i = 1
        backTrack(i, curSum , st, count)

        
        return self.result
        