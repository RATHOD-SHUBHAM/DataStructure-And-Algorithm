class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    def leaders(self, A, N):
        leader = []
        
        currentLeader = A[N-1]
        
        for i in reversed(range(N)):
            curNum = A[i]
            
            if curNum >= currentLeader:
                leader.append(curNum)
                currentLeader = curNum
                
        return leader[::-1]
            