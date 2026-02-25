# Tc :O(n x m) , where n is len of strs and m is len of shortest string, 
# we say len of shortest string because we stop the iteration of for i in range(len(prefix)), when i == len(s) where s can be shortest string
# Sc: O(m), where m is len of shortest string.
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
