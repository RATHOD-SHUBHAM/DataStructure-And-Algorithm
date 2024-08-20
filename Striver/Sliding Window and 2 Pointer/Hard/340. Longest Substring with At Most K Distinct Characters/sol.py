# Tc: O(n) | Sc: O(k)

from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        n = len(s)

        freq = collections.defaultdict(int)

        left = right = 0

        long_substring = 0

        while right < n:
            freq[s[right]] += 1

            while len(freq) > k:
                freq[s[left]] -= 1

                if freq[s[left]] == 0:
                    del freq[s[left]]
                
                left += 1
            
            cur_len = right - left + 1

            long_substring = max(long_substring , cur_len)

            right += 1
        
        return long_substring