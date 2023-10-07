# Tc Sc : O(n)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)

        if n == 0:
            return 0

        left = right = 0
        dic = {}
        longest_sub = 0

        while right < n:
            if s[right] not in dic or dic[s[right]] < left:
                dic[s[right]] = right

                cur_len = right - left + 1

                longest_sub = max(longest_sub , cur_len)

                right += 1
                             
            else:
                left = dic[s[right]] + 1
                dic[s[right]] = right
                right += 1

        return longest_sub
