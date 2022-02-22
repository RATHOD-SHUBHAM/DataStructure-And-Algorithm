'''

1048. Longest String Chain
Medium


You are given an array of words where each word consists of lowercase English letters.

wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA without changing the order of the other characters to make it equal to wordB.

For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".
A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is a predecessor of word2, word2 is a predecessor of word3, and so on. A single word is trivially a word chain with k == 1.

Return the length of the longest possible word chain with words chosen from the given list of words.

 

Example 1:

Input: words = ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: One of the longest word chains is ["a","ba","bda","bdca"].
Example 2:

Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
Output: 5
Explanation: All the words can be put in a word chain ["xb", "xbc", "cxbc", "pcxbc", "pcxbcf"].
Example 3:

Input: words = ["abcd","dbqca"]
Output: 1
Explanation: The trivial word chain ["abcd"] is one of the longest word chains.
["abcd","dbqca"] is not a valid word chain because the ordering of the letters is changed.
 

Constraints:

1 <= words.length <= 1000
1 <= words[i].length <= 16
words[i] only consists of lowercase English letters.





'''



# Time = O(nlogn + n + m^2)
# Space = O(mn)
# m = length of longest element in array
# n = no of element in array

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # sort the words  : O(nlogn)
        words = sorted(words, key = len)
        
        # O(n)
        cache = {}
        for word in words:
            cache[word] = {
                "nextWord" : "",
                "max_chain_Len" : 1
            }
        
        for word in words:
            self.findMaxChainlen(word, cache)
            
        return self.maxChainLen(cache,words)
    
    # O(m^2)
    def findMaxChainlen(self,word, cache):
        # remove one word and check if it is present in list
        for i in range(len(word)):
            smaller_word = self.breakword(i, word)
            
            if smaller_word not in cache:
                continue
                
            self.updateCache(smaller_word, word, cache)
            
    # O(n)
    def breakword(self,i, word):
        return word[ : i] + word[ i+1 : ]
    
    def updateCache(self, smaller_word, word, cache):
        smaller_word_len = cache[smaller_word]["max_chain_Len"]
        cur_word_len = cache[word]["max_chain_Len"]
        
        if smaller_word_len + 1 > cur_word_len:
            cache[word]["max_chain_Len"] = smaller_word_len + 1
            cache[word]["nextWord"] = smaller_word
            
    def maxChainLen(self, cache, words):
        maxLen = 0
        
        for word in words:
            if cache[word]["max_chain_Len"] > maxLen:
                maxLen = cache[word]["max_chain_Len"]
                
        return maxLen
        