# take the ascii 
# Tc and SC: O(nK)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list) # O(n)
        
        # O(n)
        for s in strs:
            count = [0] * 26 # take all 26 character
            
            # O(k)
            for c in s:
                count[ord(c) - ord('a')] += 1 # for that particular character change the flag
                # print(count)
                
            ans[tuple(count)].append(s)
            # print(ans)
            # print("\n")
            
            
        return ans.values()
            
        
            