# Tc: O(n^3) | Sc:O(n^2)

class Solution:
    def isPalindrome(self, x):
        n = len(x)

        left = 0
        right = n - 1

        while left <= right:
            if x[left] != x[right]:
                return False
            left += 1
            right -= 1
        return True

    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        LPS = []

        for i in range(n): #n
            for j in range(i, n): #n
                if self.isPalindrome(s[i:j+1]): #n
                    LPS.append(s[i:j+1])
        
        # print(LPS)
        max_len_palindorme = 0
        longest_LPS = LPS[0]

        for strs in LPS:
            if len(strs) > max_len_palindorme:
                max_len_palindorme = len(strs)
                longest_LPS = strs
        
        return longest_LPS


# -----------------------------------------------------------------

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