# Tc : O(m . n) | Sc: O(n)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)

        # Create a key of sorted values
        for s in strs:
            char_lst = [0] * 26 # key

            for char in s:
                idx = ord('a') - ord(char)
                char_lst[idx] += 1

            ans[str(char_lst)].append(s)
        
        return ans.values()