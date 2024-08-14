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

