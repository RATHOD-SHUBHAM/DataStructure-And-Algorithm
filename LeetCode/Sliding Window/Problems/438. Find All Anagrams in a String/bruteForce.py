'''
438. Find All Anagrams in a String

Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
 

Constraints:

1 <= s.length, p.length <= 3 * 104
s and p consist of lowercase English letters.

'''

# Brute Force
# Time Complexity :  O(n^2)
# Space Complexity : O(n)

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        output = []
        
        # base case
        if len(p) > len(s): return output
        
        pdict = collections.Counter(p)
        # print(pdict)
        
        k = len(p)
        
        for i in range(len(s) - k + 1):
            sdict = collections.Counter(s[i:i+k])
            # print(sdict)
            
            if sdict == pdict:
                output.append(i)
                
        return output