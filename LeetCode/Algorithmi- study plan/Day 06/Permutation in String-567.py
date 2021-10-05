'''

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

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # base condition
        if len(s1) > len(s2):
            return False
        
        s1_counter = Counter(s1)
        s2_counter = Counter()
        
        for idx,val in enumerate(s2):
            # add element to counter with value 1
            s2_counter[val] += 1
            
            if idx >= len(s1):
                #check the left element
                lft_ele = s2[idx - len(s1)]
                
                if s2_counter[lft_ele] == 1:
                    del s2_counter[lft_ele]
                else:
                    s2_counter[lft_ele] -= 1
                    
            if s1_counter == s2_counter:
                return True
            
        return False