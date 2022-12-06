# Tc: O(n^2) | Sc: O(n)
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        i = 1
        while i < len(words):
            prev_count = [0] * 26
            cur_count = [0] * 26
            
            prev_char = words[i-1]
            cur_char = words[i]
            
            for ch in prev_char:
                ascii_value = ord(ch) - ord("a")
                prev_count[ascii_value] += 1
            
            for ch in cur_char:
                ascii_value = ord(ch) - ord("a")
                cur_count[ascii_value] += 1
                
            if cur_count == prev_count:
                words.remove(cur_char)
                i -= 1
                
            i += 1
        
        return words