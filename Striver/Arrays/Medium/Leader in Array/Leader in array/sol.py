class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    def leaders(self,n, arr):
        #Code here
        
        leaders = []
        
        cur_leader = arr[-1]
        
        for i in reversed(range(n)):
            cur_num = arr[i]
            
            if cur_num >= cur_leader:
                # Update the leader
                leader = cur_num
                leaders.append(leader)
                
        
        return leaders[::-1]