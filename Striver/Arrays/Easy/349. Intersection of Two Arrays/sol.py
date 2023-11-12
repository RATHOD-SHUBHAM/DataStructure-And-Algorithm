# Tc and Sc: O(m + n)

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        
        ans = []
        set_1 = set(nums1)
        set_2 = set(nums2)

        for i in set_2:
            if i in set_1:
                ans.append(i)
        
        return ans