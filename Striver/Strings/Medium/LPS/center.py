# Expand form center
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        LPS = ""
        max_len = 0

        for i in range(n):
            
            # Odd len substring
            left = right = i

            while left >= 0 and right < n and s[left] == s[right]:
                cur_len = (right - left) + 1

                if cur_len > max_len:
                    max_len = cur_len
                    LPS = s[left : right + 1]
                
                # Expand from center
                left -= 1
                right += 1

            
            # Even len substring
            left = i
            right = i + 1

            while left >= 0 and right < n and s[left] == s[right]:
                cur_len = (right - left) + 1

                if cur_len > max_len:
                    max_len = cur_len
                    LPS = s[left : right + 1]

                # Expand from center
                left -= 1
                right += 1
        
        return LPS