class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        m = len(t)

        if n < m:
            return ""

        freq = collections.defaultdict(int)

        # pre inserted value
        for x in t:
            freq[x] += 1

        count = 0

        min_window_len = math.inf
        
        left = right  = 0

        while right < n:
            # Check if the cur character was pre inserted - meaning its present in t
            if freq[s[right]] > 0:
                count += 1
            
            # add to current window
            freq[s[right]] -= 1

            # Check if all the char in t are present in current window
            while count == m:
                # calculate the window size
                cur_window_len = (right - left) + 1
                if cur_window_len < min_window_len:
                    start_idx = left # mark the min wondow start
                    min_window_len = cur_window_len

                # Remove from the current window
                freq[s[left]] += 1

                if freq[s[left]] > 0:
                    count -= 1
                
                left += 1
                

            right += 1
        
        if min_window_len == math.inf:
            return ""
        else:
            return s[start_idx : start_idx + min_window_len]
