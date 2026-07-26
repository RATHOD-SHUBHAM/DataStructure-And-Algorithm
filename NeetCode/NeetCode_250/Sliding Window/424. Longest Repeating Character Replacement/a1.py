# ------------------------- Brute Force ----------------------------------

'''
https://www.youtube.com/watch?v=_eNhaDCr6P0&t=721s

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

                # No of character to flip
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

        # freq[c] = count of character c in current window [left, right]
        freq = defaultdict(int)

        longest_rcp = 0

        while right < n:
            # Expand window: include s[right]
            freq[s[right]] += 1

            cur_window_size = right - left + 1

            # Recompute majority letter count in the current window.
            # NOTE: max(freq.values()) scans ALL keys in freq every call —
            # this makes each check O(26) instead of O(1), since freq can
            # hold stale/zero entries for letters no longer in the window.
            # Doesn't break correctness, but costs a constant-factor slowdown.
            max_freq = max(freq.values())

            # Cost to convert this window into all-one-letter:
            # replace every non-majority character
            # Take the whole window, and subtract out the majority letter's count.
            # What's left over is exactly the non-majority characters —
            # i.e. the ones that would need to be flipped to match the majority letter.
            no_of_flip = cur_window_size - max_freq

            # If cost exceeds budget k, shrink from the left until valid again
            while no_of_flip > k:
                # Remove s[left] from window
                freq[s[left]] -= 1
                left += 1

                # Recompute window size and majority count after shrinking
                cur_window_size = right - left + 1
                max_freq = max(freq.values())
                no_of_flip = cur_window_size - max_freq

            # Window [left, right] is now valid — update best answer
            longest_rcp = max(longest_rcp, cur_window_size)

            right += 1

        return longest_rcp


# ------------------------- Without Comment ----------------------------------

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)

        left = right = 0

        window = collections.defaultdict(int)

        lcr = 0

        while right < n:

            # add to current window
            window[s[right]] += 1

            cur_widow_len = (right - left) + 1

            # compute no of flip
            max_freq_ele = max(window.values()) # return the element that occurs max time in the current window

            no_of_flip = cur_widow_len - max_freq_ele # this will tell about the remaining element that can be flipped

            while no_of_flip > k:
                # Shrink the current window
                window[s[left]] -= 1

                left += 1

                cur_widow_len = (right - left) + 1

                # compute no of flip
                max_freq_ele = max(window.values()) # return the element that occurs max time in the current window

                no_of_flip = cur_widow_len - max_freq_ele # this will tell about the remaining element that can be flipped
            

            lcr = max(lcr , cur_widow_len)
            
            right += 1
        
        return lcr

