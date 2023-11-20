class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)

        total_len = m + n

        mid = total_len // 2

        idx_1 = mid
        idx_2 = mid - 1

        val_at_idx_1 = -1
        val_at_idx_2 = -1
        

        i = 0
        j = 0

        count = 0

        while i < m and j < n:
            if count > idx_1:
                break
            
            if nums1[i] < nums2[j]:
                if count == idx_1:
                    val_at_idx_1 = nums1[i]
                if count == idx_2:
                    val_at_idx_2 = nums1[i]
                
                count += 1
                i += 1
            
            elif nums2[j] > nums1[i]:
                if count == idx_1:
                    val_at_idx_1 = nums2[j]
                
                if count == idx_2:
                    val_at_idx_2 = nums2[j]

                count += 1
                j += 1


        # remaining value
        while i < m:
            if count > idx_1:
                break

            if count == idx_1:
                val_at_idx_1 = nums1[i]
            if count == idx_2:
                val_at_idx_2 = nums1[i]
            
            count += 1
            i += 1

        while j < n:
            if count > idx_1:
                break

            if count == idx_1:
                val_at_idx_1 = nums2[j]
            
            if count == idx_2:
                val_at_idx_2 = nums2[j]

            count += 1
            j += 1


        # calculate median
        if total_len % 2 == 1:
            return val_at_idx_1
        else:
            median = (val_at_idx_1 + val_at_idx_2) / 2
            return median