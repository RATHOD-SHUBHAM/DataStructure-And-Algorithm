# Tc: O(n) | Sc: O(1)
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        xor = 0
        for num in nums:
            xor ^= num
        return xor

# --------------------------------------------------------------------------------------------------------------------------------------------

"""
Trick:
Like the original array, the subarray containing the single element must be odd-lengthed. The subarray not containing it must be even-lengthed. 
So by taking a pair out of the middle and then calculating which side is now odd-lengthed, we have the information needed for binary search.
"""
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)

        left = 0
        right = n - 1

        while left < right:
            mid = left + (right - left) // 2

            if mid - 1 != -1 and nums[mid] == nums[mid - 1]:
                '''There is a duplicate on left'''
                is_rightside_oddlen = (right - mid) % 2 != 0

                if is_rightside_oddlen:
                    left = mid + 1
                else:
                    right = mid - 2
            
            elif mid + 1 != n and nums[mid] == nums[mid + 1]:
                '''There is a duplicate on right'''
                is_rightside_oddlen = (right - (mid+1 )) % 2 != 0

                if is_rightside_oddlen:
                    left = mid + 2
                else:
                    right = mid - 1
            
            else:
                return nums[mid]
        
        return nums[left]