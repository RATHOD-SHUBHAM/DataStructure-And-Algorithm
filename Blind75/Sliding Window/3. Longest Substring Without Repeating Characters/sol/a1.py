# Using Set

# Tc Sc : O(n)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)

        if not s:
            return 0

        unique_char = set()

        left = right = 0

        longest_subsequence = 1

        while right < n:
            if s[right] not in unique_char:
                unique_char.add(s[right])

                # get current length
                cur_len = right - left + 1

                longest_subsequence = max(longest_subsequence, cur_len)

                right += 1
            
            else:
                # Remove element from left one by one
                while s[right] in unique_char:
                    unique_char.remove(s[left])
                    left += 1

        return longest_subsequence
    

# ------------------------------------------------------------

# Using Dictionary

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
