'''
1763. Longest Nice Substring

A string s is nice if, for every letter of the alphabet that s contains, it appears both in uppercase and lowercase. For example, "abABB" is nice because 'A' and 'a' appear, and 'B' and 'b' appear. However, "abA" is not because 'b' appears, but 'B' does not.

Given a string s, return the longest substring of s that is nice. If there are multiple, return the substring of the earliest occurrence. If there are none, return an empty string.

 

Example 1:

Input: s = "YazaAay"
Output: "aAa"
Explanation: "aAa" is a nice string because 'A/a' is the only letter of the alphabet in s, and both 'A' and 'a' appear.
"aAa" is the longest nice substring.
Example 2:

Input: s = "Bb"
Output: "Bb"
Explanation: "Bb" is a nice string because both 'B' and 'b' appear. The whole string is a substring.
Example 3:

Input: s = "c"
Output: ""
Explanation: There are no nice substrings.
Example 4:

Input: s = "dDzeE"
Output: "dD"
Explanation: Both "dD" and "eE" are the longest nice substrings.
As there are multiple longest nice substrings, return "dD" since it occurs earlier.
 

Constraints:

1 <= s.length <= 100
s consists of uppercase and lowercase English letters.

'''

# Time complexity: O(n)
# space complexity: O(1)


class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        
        if len(s) <= 1:
            return ""
        
        subset = set(s)
        
        for i,ch in enumerate(s):
            # if both upper and lower case letter not in subset then there is no nice pair for that character. So divide the pair at that point
            if ch.lower() not in subset or ch.upper() not in subset:
                leftSet = self.longestNiceSubstring(s[:i])
                rightSet = self.longestNiceSubstring(s[i+1:])
                
                # "dDzeE" if both left and right set are same we have to return left
                return leftSet if len(leftSet) >= len(rightSet) else rightSet
            
        return s