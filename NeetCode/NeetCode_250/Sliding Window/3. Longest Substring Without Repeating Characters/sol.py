class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)

        if n < 1:
            return 0

        dic = {}

        left = 0
        right = 0

        max_dist = 1

        while right < n:
            if s[right] in dic:
                # Check if dic[s[right]] is part of current window
                if dic[s[right]] >= left:
                    cur_dist = right - left
                    max_dist = max(max_dist, cur_dist)

                    left = dic[s[right]] + 1
            
            dic[s[right]] = right
            right += 1
        
        cur_dist = right - left
        max_dist = max(max_dist, cur_dist)
        
        return max_dist
    
# =====================================================================

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)

        if n < 1:
            return 0

        dic = {}

        left = 0
        right = 0

        max_dist = 1

        while right < n:

            # Check if dic[s[right]] is part of current window and if new left is after the old left, because we cannot be going back
            # eg: "tmmzuxt"
            if s[right] in dic and dic[s[right]] >= left: # Check if there are duplicate in current window
                left = dic[s[right]] + 1
            
            cur_dist = (right - left) + 1
            max_dist = max(max_dist, cur_dist)

            dic[s[right]] = right

            right += 1
        
        return max_dist