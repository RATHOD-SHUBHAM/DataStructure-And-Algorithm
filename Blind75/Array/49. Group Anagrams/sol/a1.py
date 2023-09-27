# Sort

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

# =====================================================================

# Count

# Tc: O(nk) | Sc: O(n)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)

        # O(k)
        for s in strs:
            count = [0] * 26

            # O(n)
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            # print(count)

            ans[tuple(count)].append(s)

            # print(ans)
            # break
        
        return ans.values()
          