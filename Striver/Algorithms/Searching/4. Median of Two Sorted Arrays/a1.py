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

# Solve using symmentry

from typing import List
import math

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)

        if m > n:
            """
                This is just to reduce the time complexity,
                log(n - 1) will have lessesr time complexity than log(n)
                so that is why we perform binary search on smaller array 
            """
            return self.findMedianSortedArrays(nums2 , nums1)

        V = m + n

        #Step 1: Total number of elements needed on left side of final array
        left_side = (m + n + 1) // 2 # +1 in case of odd size array

        # Step 2: Pick the left and right side element
        '''
            We can either choose 0 elements or all elements from an array
            so initially we can have 
            left = 0 -> 0 elements
            right = m -> all elements
        '''
        left = 0
        right = m

        while left <= right:
            '''
                arr1 = mid1 = # of element from nums1
                arr2 = mid2 = # of element from nums2
            '''
            mid1 =(left + right) // 2
            mid2 = left_side - mid1

            # step 2.1 : assign pointers
            # calculate symmetry
            l1 = l2 = -math.inf # since this is left portion, we always take small value
            r1 = r2 = math.inf # since this is right portion, we always take large value

            # assign the symmetry pointers
            if mid1 < m:
                r1 = nums1[mid1]
            if mid2 < n:
                r2 = nums2[mid2]
            if mid1 - 1 >= 0:
                l1 = nums1[mid1 - 1]
            if mid2 - 1 >= 0:
                l2 = nums2[mid2 - 1]

            # step 2.2 : Check if this form the perfect symmetry
            """
            We will only check the symmertries -> Why?
            Because l1 will always be less than r1, and l2 will always be less that r2
            why?
            Because l1 belong the same array as r1, and this array is already sorted
            similarly
            l2 belong the same array as r2, and this array is already sorted
            """
            if l1 <= r2 and l2 <= r1:
                if V % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2
                else:
                    return max(l1 ,l2)
            elif l1 > r2:
                # reduce count of l1
                right = mid1 - 1
            else:
                # increase count of l1
                left = mid1 + 1
        
        return -1
