import math
from typing import List

# Tc and Sc: O(n + m) 
def medianOfTwoSortedArrays(arrayOne, arrayTwo):
    n1 = len(arrayOne)
    n2 = len(arrayTwo)

    sortedArray = []

    p = q = 0

    while p < n1 and q < n2:
        if arrayOne[p] < arrayTwo[q]:
            sortedArray.append(arrayOne[p])
            p += 1
        else:
            sortedArray.append(arrayTwo[q])
            q += 1

    sortedArray += arrayOne[p : ] + arrayTwo[q : ]


    n = len(sortedArray)
    mid = n // 2

    if n % 2 == 0:
        
        median = (sortedArray[mid] + sortedArray[mid-1]) / 2
        return median
    else:
        return sortedArray[mid]


# ----------- Symmetry Algorithm ----------
# Explanation in symmetry.py

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)

        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)

        # step 1: Identify how many element on each side
        left_side = (m + n + 1) // 2

        # step 2: Identify how many element on left from each array
        left = 0
        right = m

        while left <= right:

            mid1 = (left + right) // 2
            mid2 = left_side - mid1

            # 2.1: Assign pointers
            l1 = l2 = -math.inf
            r1 = r2 = math.inf

            if mid1 < m:
                r1 = nums1[mid1]
            if mid2 < n:
                r2 = nums2[mid2]
            
            if mid1 - 1 >= 0:
                l1 = nums1[mid1 - 1]
            if mid2 - 1 >= 0:
                l2 = nums2[mid2 - 1]
            
            # 2.2: Check for symmetry
            if l1 <= r2 and l2 <= r1:
                if (m+n) % 2 == 0:
                    median = (max(l1, l2) + min(r1, r2)) / 2
                    return median
                else:
                    median = max(l1, l2)
                    return median
            elif l1 > r2:
                right = mid1 - 1
            else:
                left = mid1 + 1
        
        return -1