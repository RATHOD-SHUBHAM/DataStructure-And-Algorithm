# Time Complexity: O(S) where S = total number of characters across all strings
# Space Complexity: O(M) where M = length of the shortest string


#  Note: A prefix must start from the beginning of each string. 

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        prefix = strs[0] # the max len of common prefix will be len of our smallest char in worst case

        lcp = ""

        for i in range(len(prefix)): # O(m)
            # Simulatenously iterate and compare each character
            for s in strs: # O(n)
                if i == len(s) or s[i] != prefix[i]:
                    return lcp
                
            lcp += prefix[i]
        
        return lcp
