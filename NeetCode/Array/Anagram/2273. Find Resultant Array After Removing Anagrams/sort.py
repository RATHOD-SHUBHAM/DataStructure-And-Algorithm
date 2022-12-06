# Tc: O(nlogn) | Sc: O(1)
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        i = 1
        while i < len(words):    
            prev_char = sorted(words[i-1])
            cur_char = sorted(words[i]) 
                
            if prev_char == cur_char:
                words.remove(words[i])
                i -= 1
                
            i += 1
        
        return words