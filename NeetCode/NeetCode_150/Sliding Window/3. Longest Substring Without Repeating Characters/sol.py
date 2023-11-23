class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)

        unique_char = {}

        left = right = 0

        max_window_size = 0

        while right < n:
            '''
                If a char is in dic and left has crossed that char then that char is not part of current substring.

                eg: a b b a:
                        l r
                
                dic = {a : o
                        b= 2}

                now right is at index 2 and a is present in dictionary, but we would consider current a because our new subset is startign from index 2 

            '''

            if s[right] in unique_char and left <= unique_char[s[right]]:
                left = unique_char[s[right]] + 1

            cur_window_size = (right - left) + 1

            max_window_size = max(max_window_size , cur_window_size)

            unique_char[s[right]] = right

            right += 1
        
        return max_window_size