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
                