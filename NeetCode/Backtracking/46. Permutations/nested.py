class Solution:
    def __init__(self):
        self.result = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        visited = [False] * n

        def backTrack():

            if len(st) == n:
                self.result.append(st.copy())
                return
            
            for i in range(n):
                if visited[i] == True:
                    continue

                st.append(nums[i])
                visited[i] = True

                backTrack()

                st.pop()
                visited[i] = False
            
            return
        

        st = []
        backTrack()

        return self.result