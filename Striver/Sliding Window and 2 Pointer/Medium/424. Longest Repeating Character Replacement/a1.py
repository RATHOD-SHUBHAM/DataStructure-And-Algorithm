# ------------------------- Brute Force ----------------------------------

'''
For a given string - in order to make all the characters as same, We try to change the character that has min freq.

no_of_flips = len(string) - max_freq

eg:  A A B A B A

A = 4 , B = 2
n = 6
 In order to make all the string as same, i  need to flip 2 Bs, becasue they are small in number rather than flipping all As

no_of_flips = 6 - 4 = 2 // this is the no of b i need to flip

'''
from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)

        longest_rcp = 0

        for i in range(n):
            
            freq = defaultdict(int)
            max_freq = -math.inf

            for j in range(i, n):

                freq[s[j]] += 1

                cur_window_size = j - i + 1
                max_freq = max(freq.values())

                # No of character to file
                no_of_flip = cur_window_size - max_freq

                if no_of_flip <= k:
                    longest_rcp = max(longest_rcp , cur_window_size)
                else:
                    break
        
        return longest_rcp
    
# ------------------------- Better ----------------------------------

from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)

        left = right = 0

        freq = defaultdict(int)

        longest_rcp = 0

        while right < n:
            freq[s[right]] += 1

            cur_window_size = right - left + 1
            max_freq = max(freq.values())

            no_of_flip = cur_window_size - max_freq

            if no_of_flip <= k:
                longest_rcp = max(longest_rcp, cur_window_size)
            else:
                while no_of_flip > k:
                    # Shrink the window
                    freq[s[left]] -= 1
                    left += 1
                
                    cur_window_size = right - left + 1
                    max_freq = max(freq.values())
                    no_of_flip = cur_window_size - max_freq
                
                longest_rcp = max(longest_rcp, cur_window_size)
            
            right += 1

        return longest_rcp

# ------------------------- Optimal ----------------------------------

from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)

        left = right = 0

        freq = defaultdict(int)

        longest_rcp = 0

        while right < n:
            freq[s[right]] += 1

            cur_window_size = right - left + 1
            max_freq = max(freq.values())

            no_of_flip = cur_window_size - max_freq

            
            while no_of_flip > k:
                # Shrink the window
                freq[s[left]] -= 1
                left += 1
            
                cur_window_size = right - left + 1
                max_freq = max(freq.values())
                no_of_flip = cur_window_size - max_freq
            
            longest_rcp = max(longest_rcp, cur_window_size)
            
            right += 1

        return longest_rcp

