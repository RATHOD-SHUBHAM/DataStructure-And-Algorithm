"""
We iterate through the string and track the sizes of consecutive groups of 0s or 1s.

As we move from one character to the next:

If the character changes, we just finished one group and started a new one.

We can now compute how many valid substrings can be formed using the previous group and the current group.
"""

#Tc: O(n)
#Sc: O(1)

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        n = len(s)

        count = 0

        # prev_group stores the size of the previous group of consecutive 0s or 1s
        prev_group = 0 
        # cur_group stores the size of the current group of consecutive 0s or 1s
        cur_group = 1

        idx = 1

        while idx < n:
            # If the current character is different from the previous one, 
            # it indicates the end of a group and the start of a new group
            if s[idx-1] != s[idx]:
                cur_substring_count = min(prev_group, cur_group)
                count += cur_substring_count

                # Reset the group size
                prev_group = cur_group
                cur_group = 1 # reset the count of current group
            
            else:
                # If the character is the same, increment the size of the current group
                cur_group += 1
            
            idx += 1
        
        # For the last group
        cur_substring_count = min(prev_group, cur_group)
        count += cur_substring_count


        return count