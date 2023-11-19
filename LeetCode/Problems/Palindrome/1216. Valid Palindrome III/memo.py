# TLE

class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        n = len(s)
        memo = {}
        
        left = 0
        right = n - 1
        return self.backTrack(left , right, memo, s) <= k
    
    def backTrack(self, left , right, memo, s):
        # base case
        # if there is only one letter
        if left == right:
            return 0
        
        # if there are 2 letters: eg ab
        if left == right - 1:
            if s[left] == s[right]:
                return 0
            else:
                return 1
        
        key = (left , right)
        if key is memo:
            return memo[key]
        
        # if the letters match
        if s[left] == s[right]:
            memo[key] = self.backTrack(left + 1 , right - 1, memo, s)
        else:
            # 1 + because- this means Ill be removing one character, and checking if the substring are palindrome
            # min because, out of the 2 substring, I want the one where ill have minimun replacment that will form the substring
            memo[key] = 1 + min (
                self.backTrack(left + 1 , right, memo, s) , 
                self.backTrack(left , right - 1, memo, s)
            )
            
        return memo[key]