'''

438. Find All Anagrams in a String
Medium


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


# problem statement makes no guarantees on which string is larger that is why O(n+m)
# Time and Space = O(n+m) || O(1)

from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        op = []
        len_s = len(s)
        len_p = len(p)
        
        if len_s < len_p:
            return op
        
        # initialise counter
        counter_s = Counter()
        counter_p = Counter(p)
        
        for i in range(len_s):
            counter_s[s[i]] += 1
            
            # if window size become greater than or equal to p (index is taken to consideration so equal toz)
            if i >= len_p:
                # if counter value of first ele equal to 1 del else reduce its value
                if counter_s[s[i - len_p]] == 1:
                    del counter_s[s[i - len_p]]
                else:
                    counter_s[s[i-len_p]] -= 1
                    
            if counter_s == counter_p:
                op.append(i - len_p + 1)
                
        return op