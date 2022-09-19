# 3 pointer approach
# time = O(m + n)
# space = O(1)


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        # base case
        if len(nums1) < m + n:
            return
        
        # assigning 2 pointers
        p = m - 1
        q = n - 1
        
        
        for i in reversed(range(len(nums1))):
            if q < 0 or (p >= 0 and nums1[p] > nums2[q]):
                nums1[i] = nums1[p]
                p -= 1
            else:
                nums1[i] = nums2[q]
                q -= 1
                
        return nums1