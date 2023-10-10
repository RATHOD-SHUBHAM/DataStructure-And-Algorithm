'''
    We create a list called filtered_S 
    which has all the characters from string S along with their indices in S, 
    but these characters should be present in T.
'''

'''
    S = "ABCDDDDDDEEAFFBC" T = "ABC"
    filtered_S = [(0, 'A'), (1, 'B'), (2, 'C'), (11, 'A'), (14, 'B'), (15, 'C')]
    Here (0, 'A') means in string S character A is at index 0.
'''

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