class Solution:
    def anagram(self, word_1, word_2):
        return sorted(word_1) == sorted(word_2)

    def removeAnagrams(self, words: List[str]) -> List[str]:
        # This will be a problem
        n = len(words)  
        

        idx = 1

        # while idx < n:
        #     # After deleting an item with del words[idx], the length n of the list shrinks, but n isn't updated in the loop condition.
        #     while idx < n and self.anagram(words[idx - 1] , words[idx]) == True:
        while idx < len(words):
            while idx < len(words) and self.anagram(words[idx - 1] , words[idx]) == True:
                del words[idx]

            idx += 1
            
        return words
    
# Avoid in-place deletion altogether (cleaner and safer)