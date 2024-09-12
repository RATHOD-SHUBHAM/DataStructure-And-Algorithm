# Tc: O(m + n . k) If the k is the length of the longest word, this takes O(n⋅k) time.
# Sc: O(1)

# Same as solution one but using set
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set(allowed)

        count = 0
        for word in words:
            flag = True
            word_set = set(word)

            for ch in word_set:
                if ch not in allowed_set:
                    flag = False
                    break
            
            if flag == True:
                count += 1
        
        return count
            