'''

567. Permutation in String
Medium


Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.


'''


# sliding window + hash map

from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # base case
        if len(s1) > len(s2):
            return False
        
        # create counter for s1 and s2
        s1_counter = Counter(s1)
        s2_counter = Counter()
        
        for i in range(len(s2)):
            
            # add s2[i] in dict and compare it with s1
            s2_counter[s2[i]] += 1

            
            # if the window size is equal to or more than s1
            if i >= len(s1):
                left_most = i - len(s1)
                
                # if the left most element occured only once --  delete it
                if s2_counter[s2[left_most]] == 1:
                    del s2_counter[s2[left_most]]
                # if left most element occured more than once -- reduce its count by 1
                else:
                    s2_counter[s2[left_most]] -= 1
            
            
            if s1_counter == s2_counter:
                return True
        
        return False