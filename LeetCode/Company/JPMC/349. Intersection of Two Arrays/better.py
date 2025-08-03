# Tc :O(m + n)
# Sc: O(n)

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m = len(nums1)
        n = len(nums2)

        # Making sure m is always greater than n
        # This can be skipped, but just making sure that in later step we traverse the smaller array rather than the larger one
        if m < n:
            return self.intersection(nums2, nums1)
        
        # Logic
        set_nums1 = set(nums1)
        
        op = []
        for num in nums2:
            if num in set_nums1:
                op.append(num)
                set_nums1.remove(num) # Remove the element from set to make it unique


        return op