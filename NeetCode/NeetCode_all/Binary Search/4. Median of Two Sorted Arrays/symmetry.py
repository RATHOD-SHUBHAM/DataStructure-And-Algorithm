class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)

        # perform binary search on smaller array , since it is easier
        # we always try to keep first array smaller
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)

        # total length
        V = m + n

        # No of element on the left symmetry
        left_side = (m + n + 1) // 2

        left = 0
        right = m

        while left <= right:
            # no of element to take from nums1 to form left symmetry
            mid_1 = (left + right) // 2
            # take the remaining elements from nums2 to form left symmetry
            mid_2 = left_side - mid_1

            # calculate l1 , l2, r1, r2
            l1 = l2 = -math.inf
            r1 = r2 = math.inf

            if mid_1 < m:
                r1 = nums1[mid_1]
            if mid_2 < n:
                r2 = nums2[mid_2]
            
            if mid_1 - 1 >= 0:
                l1 = nums1[mid_1 - 1]
            if mid_2 - 1 >= 0:
                l2 = nums2[mid_2 - 1]

            
            # calculate median
            if l1 <= r2 and l2 <= r1:
                if V % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2
                else:
                    return max(l1, l2)
            # move the pointers if none of above condition match
            elif l1 > r2:
                # taken more values from num1 - need to reduce
                right = mid_1 - 1
            else:
                # need to add more value from num1
                left = mid_1 + 1

        return 0
