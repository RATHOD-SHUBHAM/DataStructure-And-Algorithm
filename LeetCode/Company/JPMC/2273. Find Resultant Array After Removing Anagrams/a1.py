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

# ------------------------- Avoiding In-place Deletion -------------------------

# Tc: O(n * k log k), where n is len(words) and k is len(each word)
# Sc: O(K) -> Counter space

class Solution:
    # O(K)
    def groupAnagram(self, word_1, word_2):
        return sorted(word_1) == sorted(word_2)

    def removeAnagrams(self, words: List[str]) -> List[str]:
        n = len(words)

        left = 0
        right = left + 1

        op = []

        # O(n)
        while right < n:
            if self.groupAnagram(words[left], words[right]) == True:
                right += 1
            else:
                op.append(words[left])

                left = right
                right = left + 1
        
        op.append(words[left])

        return op
                
# ------------------------- Better Approach -------------------------

# Tc: O(n * k), where n is len(words) and k is len(each word)
# Sc: O(k)

class Solution:
    # O(K)
    def groupAnagram(self, word_1, word_2):
        word_1_count = collections.Counter(word_1)
        # print(word_1_count)

        word_2_count = collections.Counter(word_2)
        # print(word_2_count)

        # print("==============")
        return word_1_count == word_2_count

    def removeAnagrams(self, words: List[str]) -> List[str]:
        n = len(words)

        left = 0
        right = left + 1

        op = []

        # O(n)
        while right < n:
            if self.groupAnagram(words[left], words[right]) == True:
                right += 1
            else:
                op.append(words[left])

                left = right
                right = left + 1
        
        op.append(words[left])

        return op

# ------------------------- Same Approach -------------------------

# Tc: O(n * k), where n is len(words) and k is len(each word)
# Sc: O(k)

class Solution:
    # O(K)
    def groupAnagram(self, word_1, word_2):
        word_1_count = collections.Counter(word_1)
        # print(word_1_count)

        word_2_count = collections.Counter(word_2)
        # print(word_2_count)

        # print("==============")
        return word_1_count == word_2_count

    def removeAnagrams(self, words: List[str]) -> List[str]:
        n = len(words)

        left = 0
        op = []

        # O(n)
        while left < n:
            op.append(words[left])

            right = left + 1
            while right < n and self.groupAnagram(words[left], words[right]) == True:
                right += 1
            
            
            left = right

        return op
                