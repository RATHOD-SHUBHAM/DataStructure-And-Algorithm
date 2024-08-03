# ------------------------ Sorted Set --------------------------

# Tc: O(nlogn) | Sc: O(1)

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = sorted(set(nums))
        return len(nums)
    

# ------------------------ 3 pointer -------------------------

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)

        i = 0 # keep track of the last index of unique elemet
        j = 1
        k = 1 # next index for unique element

        while j < n:
            if nums[j] == nums[i]:
                j += 1
            else:
                self.swap(k , j, nums)
                i = k
                k += 1
                j += 1
        
        return i + 1
    
    def swap(self, k, j, nums):
        nums[k], nums[j] = nums[j], nums[k]
        return
    


# ------------------------ 2 pointer -------------------------


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)

        insertPosition = 1 # next idx for unique elemet
        idx = 1

        while idx < n:
            # if not dulicate
            if nums[idx] != nums[idx - 1]:
                # this is the next position after unique character
                nums[insertPosition] = nums[idx]
                insertPosition += 1

            idx += 1
        
        # print(insertPosition)
        return insertPosition