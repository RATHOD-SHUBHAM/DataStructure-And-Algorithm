class Solution:
    def LCS(self, s1, s2):
        m = len(s1)
        n = len(s2)

        dp = [[0 for _ in range(n+1)]for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    split_1 = dp[i-1][j]
                    split_2 = dp[i][j-1]

                    dp[i][j] = max(split_1, split_2)
            
        return dp

    def length_shortestCommonSupersequence(self, str1: str, str2: str) -> int:
        """Return the length of shortest common supersequence"""
        m = len(str1)
        n = len(str2)

        dp = self.LCS(str1, str2)

        lcs = dp[m][n] # common subsequence

        # Non common words
        non_common_1 = m - lcs
        non_common_2 = n - lcs

        # Combine them together
        shortestSupersequence = non_common_1 + non_common_2 + lcs

        # or
        shortestSupersequence = (m + n) - lcs

        print(shortestSupersequence)


    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        """Return the shortest common supersequence"""
        m = len(str1)
        n = len(str2)

        dp = self.LCS(str1, str2)

        # Bactrack and get the supersequence
        supersequence = self.backtrack(str1, str2, dp, m, n)

        return supersequence[::-1]
    
    def backtrack(self, s1, s2, dp, m, n):
        i = m
        j = n

        supersequence = ""

        while i > 0 and j > 0:
            if s1[i-1] == s2[j-1]:
                # Common character - add it once
                supersequence += s1[i-1]
                i -= 1
                j -= 1
            else:
                # Non-common character - choose the one that led to current LCS value
                if dp[i-1][j] > dp[i][j-1]:
                    # LCS came from above (from s1)
                    supersequence += s1[i-1]
                    i -= 1
                else:
                    # LCS came from left (from s2)
                    supersequence += s2[j-1]
                    j -= 1
        
    
        # Add remaining characters from s1
        while i > 0:
            supersequence += s1[i-1]
            i -= 1
        
        # Add remaining characters from s2
        while j > 0:
            supersequence += s2[j-1]
            j -= 1
        
        return supersequence


# Test the solution
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    str1 = "abac"
    str2 = "cab"
    result = solution.shortestCommonSupersequence(str1, str2)
    length = solution.length_shortestCommonSupersequence(str1, str2)
    print(f"Input: str1 = '{str1}', str2 = '{str2}'")
    print(f"Shortest Common Supersequence: '{result}'")
    print(f"Length: {length}")
    print()
    
    # Test case 2
    str1 = "geek"
    str2 = "eke"
    result = solution.shortestCommonSupersequence(str1, str2)
    length = solution.length_shortestCommonSupersequence(str1, str2)
    print(f"Input: str1 = '{str1}', str2 = '{str2}'")
    print(f"Shortest Common Supersequence: '{result}'")
    print(f"Length: {length}")

    # Test case 3
    str1 = "brute"
    str2 = "groot"
    result = solution.shortestCommonSupersequence(str1, str2)
    length = solution.length_shortestCommonSupersequence(str1, str2)
    print(f"Input: str1 = '{str1}', str2 = '{str2}'")
    print(f"Shortest Common Supersequence: '{result}'")
    print(f"Length: {length}")

    # Test case 4
    str1 = "blue"
    str2 = "glue"
    result = solution.shortestCommonSupersequence(str1, str2)
    length = solution.length_shortestCommonSupersequence(str1, str2)
    print(f"Input: str1 = '{str1}', str2 = '{str2}'")
    print(f"Shortest Common Supersequence: '{result}'")
    print(f"Length: {length}")