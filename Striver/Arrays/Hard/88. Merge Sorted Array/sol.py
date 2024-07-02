class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:       
        p = m - 1
        q = n - 1

        x = len(nums1)

        # Start filling in reverse order
        for i in reversed(range(x)):
            if q < 0 or (p >= 0 and nums1[p] >= nums2[q]):
                nums1[i] = nums1[p]
                p -= 1
            elif p < 0 or (q >= 0 and nums2[q] > nums1[p]):
                nums1[i] = nums2[q]
                q -= 1
            '''
                The above statment can just be added in a else block
            else:
                nums1[i] = nums2[q]
                q -= 1
            '''
        
        return nums1