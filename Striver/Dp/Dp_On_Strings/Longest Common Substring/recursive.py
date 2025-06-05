#User function Template for python3

class Solution:
    def __init__(self):
        self.max_len = float('-inf')
        self.count = 0
    def longestCommonSubstr(self, s1, s2):
        # code here
        m = len(s1)
        n = len(s2)
        
        idx1 = m-1
        idx2 = n-1
        
        self.recursion(idx1, idx2, s1, s2)
        
        return self.max_len
    
    def recursion(self, idx1, idx2, s1, s2):
        # Base case
        if idx1 < 0 or idx2 < 0:
            self.max_len = max(self.max_len, self.count)
            self.count = 0
            return
        
        # Logic
        ## Match
        if s1[idx1] == s2[idx2]:
            self.count += 1
            return self.recursion(idx1-1, idx2-1, s1, s2)
        
        # No Match

        # Store the max length found so far
        self.max_len = max(self.max_len, self.count)
        
        # Reset Count
        self.count = 0
        split_1 = self.recursion(idx1-1, idx2, s1, s2)
        
        self.count = 0
        split_2 = self.recursion(idx1, idx2-1, s1, s2)
        
        return