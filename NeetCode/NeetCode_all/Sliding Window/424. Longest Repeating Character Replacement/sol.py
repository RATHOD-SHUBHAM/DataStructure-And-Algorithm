# Tc, Sc :O(n) 
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)

        left = right = 0

        longest_substring = -math.inf

        # Store the freq of character in the given window
        freq = {}
        for i in s:
            freq[i] = 0

        while right < n:
            window_size = (right - left) + 1

            freq[s[right]] += 1

            # check if we can replace k char
            while window_size - max(freq.values()) > k:
                freq[s[left]] -= 1
                left += 1
                window_size = (right - left) + 1
            
            longest_substring = max(longest_substring , window_size)

            right += 1
        
        return longest_substring