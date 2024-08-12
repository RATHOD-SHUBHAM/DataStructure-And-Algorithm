class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)

        if n == 0:
            return 0

        dic = {} 

        left = right = 0 # Window

        longest_substring = 0

        while right < n:

            cur_ele = s[right]

            # Make sure the left pointer doesnot move backward.
            if cur_ele in dic and left <= dic[cur_ele]:
                left = dic[cur_ele] + 1
            
            
            dic[cur_ele] = right

            window_size = right - left + 1

            longest_substring = max(longest_substring , window_size)

            right += 1
        
        return longest_substring



