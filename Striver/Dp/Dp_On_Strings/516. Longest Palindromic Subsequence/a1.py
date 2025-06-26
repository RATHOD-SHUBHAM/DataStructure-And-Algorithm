class Solution:
    def __init__(self):
        self.subseq = []

    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)

        idx = n - 1

        st = []

        self.recursion(idx, st, s)

        # print(self.subseq)

        return self.longest_palindrome()

    
    def recursion(self, idx, st, s):
        # base case
        if idx < 0:
            # strng = st[::]
            # f_strng = "".join(strng)
            # self.subseq.append(f_strng)
            self.subseq.append("".join(st[::]))
            return
        
        # Take
        st.append(s[idx])
        self.recursion(idx-1, st, s)

        # No_Take
        st.pop()
        self.recursion(idx-1, st, s)

        return
    
    
    def longest_palindrome(self):
        max_len = 0

        for st in self.subseq:
            if self.valid_palindrome(st):
                cur_len = len(st)
                max_len = max(max_len, cur_len)
        
        return max_len

    def valid_palindrome(self, st):
        n = len(st)

        left = 0
        right = n-1

        while left <= right:
            if st[left] != st[right]:
                return False
            
            left += 1
            right -= 1
        
        return True
    
# --------------------------- Recursive Approach ---------------------------
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        s_reversed = s[::-1]
        print(s_reversed)

        LCS = self.LCS(s, s_reversed)
        return len(LCS)
    
    def LCS(self, s1, s2):
        n = len(s1)

        idx1 = n - 1
        idx2 = n - 1

        return self.recursion(idx1, idx2, s1, s2)
    
    def recursion(self, idx1, idx2, s1, s2):
        # base case
        if idx1 < 0 or idx2 < 0:
            return ""
        
        # Logic
        LCS = ""
        if s1[idx1] == s2[idx2]:
            LCS += self.recursion(idx1-1, idx2-1, s1, s2)
            LCS += s1[idx1]
            return LCS
        
        split_1 = self.recursion(idx1, idx2-1, s1, s2)
        split_2 = self.recursion(idx1-1, idx2, s1, s2)

        if len(split_1) > len(split_2):
            LCS += split_1
        else:
            LCS += split_2

        return LCS
    
# --------------------------- Better Recursive ---------------------------
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        s1 = s
        s2 = s[::-1] # reverse of s


        return self.LCS(s1, s2)
    
    def LCS(self, s1, s2):
        n = len(s1)

        idx1 = n - 1
        idx2 = n - 1

        return self.recursion(idx1, idx2, s1, s2)

    def recursion(self, idx1, idx2, s1, s2):
        # Base case
        if idx1 < 0 or idx2 < 0:
            return 0
        
        # Logic
        ## Match
        if s1[idx1] == s2[idx2]:
            return 1 + self.recursion(idx1-1, idx2-1, s1, s2)
        
        ## No Match
        split_1 = 0 + self.recursion(idx1-1, idx2, s1, s2)
        split_2 = 0 + self.recursion(idx1, idx2-1, s1, s2)

        return max(split_1, split_2)

# --------------------------- Tabulation Approach ---------------------------
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        s1 = s
        s2 = s[::-1] # reverse of s

        return self.LCS(s1, s2)
    
    def LCS(self, s1, s2):
        n = len(s1)

        dp = [[0 for _ in range(n+1)]for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, n+1):
                # Match
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    split_1 = dp[i-1][j]
                    split_2 = dp[i][j-1]
                    dp[i][j] = max(split_1, split_2)
        
        return dp[n][n]

# --------------------------- Space Optimized Approach ---------------------------

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        s1 = s
        s2 = s[::-1] # reverse of s

        return self.LCS(s1, s2)
    
    def LCS(self, s1, s2):
        n = len(s1)

        dp = [0 for _ in range(n+1)]

        for i in range(1, n+1):
            temp = [0 for _ in range(n+1)]
            for j in range(1, n+1):
                # Match
                if s1[i-1] == s2[j-1]:
                    temp[j] = 1 + dp[j-1]
                else:
                    split_1 = dp[j]
                    split_2 = temp[j-1]
                    temp[j] = max(split_1, split_2)
            
            dp = temp
        
        return dp[n]