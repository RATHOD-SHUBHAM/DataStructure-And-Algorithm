#User function Template for python3
class Solution:
    def __init__(self):
        self.total = []
        
    def subsetSums(self, arr, N):
        
        def backTrack(i, curSum):
            # basecase
            if i >= N:
                self.total.append(curSum)
                return
            
            # Include the current number
            curSum += arr[i]
            backTrack(i + 1, curSum)
            
            # Donot include current number
            curSum -= arr[i]
            backTrack(i+1, curSum)
            
            return
        
        # Main Function
        curSum = 0
        i = 0
        backTrack(i, curSum)
        
        return self.total