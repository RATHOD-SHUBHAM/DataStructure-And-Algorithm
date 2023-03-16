# 2 pointer appoach

# Space and Time = O(m) | O(m+n)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if len(nums1) < m + n :
            return 
        
        
        p = 0
        q = 0
        
        # make a copy of nums1 - when we replace we might miss some value
        nums = nums1[:] # O(m) space
       

        for i in range(len(nums1)):
            if q >= n or (p < m and nums[p] < nums2[q]):
                nums1[i] = nums[p]
                p += 1
            else:
                nums1[i] = nums2[q]
                q += 1
        
        