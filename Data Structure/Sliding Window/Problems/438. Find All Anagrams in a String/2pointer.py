class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        output = []
        
        # base case
        if len(p) > len(s): return output
        
        # creating 2 dictionary
        pdict = {}
        sdict = {}
        
        for i in range(len(p)):
            pdict[p[i]] = 1 + pdict.get(p[i],0) # if the element is present add 1+value else add 1
            sdict[s[i]] = 1 + sdict.get(s[i],0)
            
        if pdict == sdict:
            output.append(0) # append the start index
            
            
        left = 0
        k = len(p)
        
        for right in range(k, len(s)):
            sdict[s[right]] = 1 + sdict.get(s[right],0)
            
            # i cant directly pop because if aba and i pop a then only b will be left but we need ba
            sdict[s[left]] -= 1
            
            if sdict[s[left]] == 0:
                sdict.pop(s[left])
                
            left += 1
            
            if sdict == pdict:
                output.append(left)
                
        return output