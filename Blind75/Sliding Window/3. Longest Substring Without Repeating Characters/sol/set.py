# Tc Sc : O(n)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)

        left = right = 0

        longest_substring = 0

        unique_char = set()

        while right < n:

            while s[right] in unique_char:
                unique_char.remove(s[left])
                left += 1

            window_size = right - left + 1

            longest_substring = max(longest_substring , window_size)

            unique_char.add(s[right])

            right += 1
        
        return longest_substring