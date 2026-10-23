# 1. ================ ================ ================ Bubble Sort ================ ================= =======================

# Tc and Sc: O(n**2)

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for _ in range(n):
            for i in range(n-1):
                if nums[i] > nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
            
        return nums

# 2. ================ ================ ================ Selection Sort ================ ================= =======================

# Tc and Sc: O(n^2)

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(n):
            min_idx = i

            # Find the index of the minimum element in the unsorted part
            for j in range(i, n):
                if nums[j] < nums[min_idx]:
                    min_idx = j
            
            
            # Swap the found minimum element with the first element of the unsorted part
            nums[i], nums[min_idx] = nums[min_idx], nums[i]
        
        return nums


# 2.1 ================ ================ ================ Exchange Sort ================ ================= =======================

class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        n = len(nums)

        for i in range(n):
            for j in range(i, n):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
        
        return nums

# 3. ================ ================ ================ Insertion Sort ================ ================= =======================
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Start from the second element, first element alone is trivially sorted
        for i in range(1, n):
            key = nums[i] # Save the element to be inserted
            
            # Compare key with elements to its left, moving backwards
            j = i-1
            while j >= 0 and key < nums[j]:
                # shift every element that is greater than the key one position to the right
                nums[j+1] = nums[j]
                j -= 1
            
            # Place key in its correct position
            nums[j+1] = key

        return nums