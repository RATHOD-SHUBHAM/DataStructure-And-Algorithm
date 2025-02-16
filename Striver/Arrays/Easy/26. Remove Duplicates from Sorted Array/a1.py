# ------------------------ Sorted Set --------------------------

# Tc: O(nlogn) | Sc: O(1)

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = sorted(set(nums))
        return len(nums)
    

# ------------------------ 3 pointer -------------------------
# Swap the values

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)

        i = 0 # keep track of the last index of unique elemet
        j = 1
        k = 1 # next index for unique element

        while j < n:
            if nums[j] == nums[i]:
                # compare with first occurance
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
# Copy the values

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        
        swap_idx = 0
        i = 1
        
        while i < n:
            if nums[i - 1] != nums[i]:
                self.swap(i-1, swap_idx, nums)
                swap_idx += 1
            
            i += 1
        
        self.swap(n-1, swap_idx, nums)

        return swap_idx + 1
    
    def swap(self, i, j, nums):
        nums[i], nums[j] = nums[j], nums[i]