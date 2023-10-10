# Tc and Sc: O(S + t)

class Solution:
    def minWindow(self, s, t):

        if not t or not s:
            return ""

        # Dictionary which keeps a count of all the unique characters in t.
        dict_t = {}
        for i in range(len(t)):
            dict_t[t[i]] = dict_t.get(t[i] , 0) + 1

        # Number of unique characters in t, which need to be present in the desired window.
        required = len(dict_t)

        # left and right pointer
        l, r = 0, 0

        # formed is used to keep track of how many unique characters in t are present in the current window in its desired frequency.
        # e.g. if t is "AABC" then the window must have two A's, one B and one C. Thus formed would be = 3 when all these conditions are met.
        formed = 0

        # Dictionary which keeps a count of all the unique characters in the current window.
        window_counts = {}

        # ans tuple of the form (window length, left, right)
        ans = float("inf"), None, None

        while r < len(s):

            # Add one character from the right to the window
            window_counts[s[r]] = window_counts.get(s[r], 0) + 1

            # If the frequency of the current character added equals to the desired count in t then increment the formed count by 1.
            if s[r] in dict_t and window_counts[s[r]] == dict_t[s[r]]:
                formed += 1

            # Try and contract the window till the point where it ceases to be 'desirable'.
            while l <= r and formed == required:

                # Save the smallest window until now.
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                # The character at the position pointed by the `left` pointer is no longer a part of the window.
                window_counts[s[l]] -= 1

                if s[l] in dict_t and window_counts[s[l]] < dict_t[s[l]]:
                    formed -= 1

                # Move the left pointer ahead, this would help to look for a new window.
                l += 1    

            # Keep expanding the window once we are done contracting.
            r += 1    

        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]


# ----------------------------------------------------------------------------

# Tc and Sc: O(S + t)

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)

        dict_t = {}
        for i in range(len(t)):
            dict_t[t[i]] = dict_t.get(t[i] , 0) + 1

        required = len(dict_t)

        filtered_s = []
        for i, char in enumerate(s):
            if char in dict_t:
                filtered_s.append((i, char))
        
        m = len(filtered_s)
        
        window_count = {}

        left = right = 0

        formed = 0

        min_window_substring = (math.inf, None, None)

        while right < m:
            window_count[filtered_s[right][1]] = window_count.get(filtered_s[right][1], 0) + 1

            if window_count[filtered_s[right][1]] == dict_t[filtered_s[right][1]]:
                formed += 1
            
            while left <= right and formed == required:
                window_size = filtered_s[right][0] - filtered_s[left][0] + 1

                if window_size < min_window_substring[0]:
                    min_window_substring = (window_size, filtered_s[left][0], filtered_s[right][0])
                
                window_count[filtered_s[left][1]] -= 1

                if window_count[filtered_s[left][1]] < dict_t[filtered_s[left][1]]:
                    formed -= 1
                
                left += 1

            right += 1

        return "" if min_window_substring[0] == math.inf else s[min_window_substring[1] : min_window_substring[2] + 1]