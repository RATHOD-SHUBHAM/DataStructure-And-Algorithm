# Tc: O(Knlogn)
# Sc: O(Kn)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)

        dic = collections.defaultdict(list)

        # O(n)
        for char in strs:
            # O(nlogn)
            sorted_char = sorted(char)
            sorted_char = "".join(sorted_char)

            dic[sorted_char].append(char)
        
        op = []
        for key, values in dic.items():
            op.append(values)
        
        return op