class Solution:
    def __init__(self):
        self.result = []
        self.st = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        visited = [False] * n

        self.backTrack(visited, n, nums)

        return self.result
    
    def backTrack(self, visited, n, nums):
        if len(self.st) == n:
            self.result.append(self.st[::])
            return
        
        for i in range(n):
            if visited[i] == True:
                continue
            
            self.st.append(nums[i])
            visited[i] = True

            self.backTrack(visited, n , nums)

            self.st.pop()
            visited[i] = False
        
        return