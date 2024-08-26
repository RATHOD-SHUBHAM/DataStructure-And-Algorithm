# Tc: O(m + n) | Sc: O(m + n)

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m = len(nums1)
        n = len(nums2)

        op = [-1] * m

        for i in range(m):
            max_val = nums1[i]

            idx_2 = nums2.index(max_val)

            # Look on right for every element
            for j in range(idx_2 + 1, n):
                cur_val = nums2[j]

                if cur_val > max_val:
                    max_val = cur_val
                    break
            
            if max_val != nums1[i]:
                op[i] = max_val
        
        return op