class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        n = len(s)
        dp = [[None for _ in range(n)] for _ in range(n)]
        
        left = 0
        right = n - 1
        # if the number of replacement is less that k value. Then we return true
        return self.backTrack(left , right, dp, s) <= k
    
    # calculate the number of replacment
    def backTrack(self, left , right, dp, s):
        # base case
        if dp[left][right] is not None:
            return dp[left][right]
        
        # if there is only one letter
        if left == right:
            return 0
        
        # if there are 2 letters: eg ab
        if left == right - 1:
            if s[left] == s[right]:
                dp[left][right] = 0
                return dp[left][right]
            else:
                dp[left][right] = 1
                return dp[left][right]

        
        # if there are more than 2 character
        # if the letters match
        if s[left] == s[right]:
            # move both the pointer inward
            dp[left][right] = self.backTrack(left + 1 , right - 1, dp, s)
        else:
            # check by replacing both the left and right value
            # 1 + because- this means Ill be removing one character, and checking if the substring are palindrome
            # min because, out of the 2 substring, I want the one where ill have minimun replacment that will form the substring
            dp[left][right] = 1 + min (
                self.backTrack(left + 1 , right, dp, s) , 
                self.backTrack(left , right - 1, dp, s)
            )
            
        return dp[left][right]