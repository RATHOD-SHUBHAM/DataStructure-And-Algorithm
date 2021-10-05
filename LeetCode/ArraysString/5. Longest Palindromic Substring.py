"""
5. Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.

"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = ""
        for i in range(n):
            odd = self.helper(s, i, i)
            even = self.helper(s, i, i + 1)
            res = max(odd, even, res, key=len)
        return res

    def helper(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]
