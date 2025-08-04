# Tc and Sc: O(n)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)

        if n < 1:
            return 0

        dic = {}

        left = 0
        right = 0

        max_len = 1

        while right < n:
            if s[right] in dic:
                # Only update left if the duplicate is within current window
                if dic[s[right]] >= left:
                
                    cur_len = right - left
                    max_len = max(max_len, cur_len)

                    left = dic[s[right]] + 1

            # Always update dictionary and advance right pointer
            dic[s[right]] = right
            right += 1

        # Check final window length
        cur_len = right - left
        max_len = max(max_len, cur_len)
        
        return max_len