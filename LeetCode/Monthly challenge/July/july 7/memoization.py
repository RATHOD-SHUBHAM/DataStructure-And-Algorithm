# Time | Space: O(m * n)
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        cache = {}
        
        if len(s1) + len(s2) != len(s3):
            return False
        
        def helper(i , j):
            # base case: When we reach the end of both string. 
            # then we are able to create string s3
            if i == len(s1) and j == len(s2):
                return True
            
            # check if the i and j value for particular branch is already there in cache
            if (i,j) in cache:
                return cache[(i,j)]
            
            #check if s3 can be formed from s1
            if i < len(s1) and s1[i] == s3[i + j] and helper(i+1 , j):
                return True
            
            # check if s3 can be formed from s2
            elif j < len(s2) and s2[j] == s3[i+j] and helper(i, j+1):
                return True
            
            # add to cache only when it is False
            cache[(i , j)] = False
            
            return False
        
        
        return helper(0 , 0)