# time: O(nklogk)
# Sc: O(nK)
# brute force : sort the characters

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        
        # O(n)
        for s in strs:
            sorted_s = sorted(s) # slogs
            # print(sorted_s)
            
            # dictionary list cannot be a hash
            sorted_s = tuple(sorted_s)
            if sorted_s not in dic:
                dic[sorted_s] = []
            
            dic[sorted_s].append(s)
            print(dic)
        
        return dic.values()