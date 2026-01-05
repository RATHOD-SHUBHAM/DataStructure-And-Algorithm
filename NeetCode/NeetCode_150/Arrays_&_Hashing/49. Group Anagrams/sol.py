# Tc and Sc: O(nk) -> n is the len of strs and k is max len of a character ch
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = collections.defaultdict(list)

        for ch in strs: # O(n)
            char = [0] * 26

            for i in range(len(ch)): # O(k)
                ltr = ord(ch[i]) - ord('a')
                char[ltr] += 1
            
            dic[tuple(char)].append((ch))

        op = []
        for key, value in dic.items():
            op.append(value)
        
        return op