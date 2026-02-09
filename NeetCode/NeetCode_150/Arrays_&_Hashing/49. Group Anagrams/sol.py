# Tc: O(NKlogK) , N is the len of strs, and K is max length of each string
# Sc: O(NK)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)

        dic = collections.defaultdict(list)

        for ch in strs: # n
            key = sorted(ch) # KlogK

            dic[tuple(key)].append(ch)
        
        op = []
        for key, val in dic.items():
            op.append(val)
        
        return op   

# ========================================================================================s

# Tc: O(NK), n is len of string, K is max len of each string
# Sc: O(N)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)

        dic = collections.defaultdict(list)

        for sts in strs: # n
            count = [0] * 26

            for ch in sts: # k
                val = ord(ch) - ord('a')

                count[val] += 1
            
            # dictionary (hash table) keys need to be hashable for comparison. An array of items is hashable if it is immutable, i.e. once it's set, it cannot be changed.
            dic[tuple(count)].append(sts)
        
        op = []
        for key, val in dic.items():
            op.append(val)
        
        return op   