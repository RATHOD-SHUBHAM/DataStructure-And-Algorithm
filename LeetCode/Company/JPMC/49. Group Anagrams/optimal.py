# Tc: O(n * m)
# Sc: O(n * m)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)

        dic = collections.defaultdict(list)

        # O(n)
        for char in strs:
            # O(m)
            count = [0] * 26 # 26 english characters

            for i in char:
                key = ord(i) - ord("a")
                count[key] += 1
            
            # List cannot be hashed because they are mutable
            dic[tuple(count)].append(char)
        
        op = []
        for key, values in dic.items():
            op.append(values)
        
        return op