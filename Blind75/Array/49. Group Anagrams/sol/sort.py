# Tc: O(knlogn) | Sc: O(nk)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)

        # O(k)
        for s in strs:
            # O(nlogn)
            sorted_s = sorted(s)

            # List cannot be keys in dictionary
            tup_s = tuple(sorted_s)

            # print(tup_s)

            ans[tup_s].append(s)

        # print(ans)
        # print(ans.values())

        return ans.values()
