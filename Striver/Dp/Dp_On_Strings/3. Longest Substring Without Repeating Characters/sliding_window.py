class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)

        left = 0
        right = 0

        dic = collections.defaultdict(int)

        cur_len = 0
        max_len = 0

        while right < n:
            # Check if this is a duplicate
            if s[right] in dic:
                prev_idx = dic[s[right]]

                # Check if the duplicate is present in the current window
                if prev_idx >= left:
                    left = dic[s[right]] + 1
            
            # Compute the dist
            cur_len = right - left + 1
            max_len = max(max_len , cur_len)

            # Update the dict
            dic[s[right]] = right

            # Move right
            right += 1
        
        return max_len
