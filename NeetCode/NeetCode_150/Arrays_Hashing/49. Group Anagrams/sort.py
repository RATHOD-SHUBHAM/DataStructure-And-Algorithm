# Tc : O(m . nlogn) | Sc: O(n)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)

        # Create a key of sorted values
        for s in strs:
            key = (str(sorted(s)))
            ans[key].append(s)
        
        # print(ans)

        return ans.values()