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


# 4. ================ ================ ================ Merge Sort ================ ================= =======================
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergesort(nums)
    
    def mergesort(self, nums):
        if len(nums) <= 1:
            return nums
        
        mid = len(nums) // 2

        # Divide
        left = self.mergesort(nums[ : mid])
        right = self.mergesort(nums[mid : ])

        return self.merge(left, right)
    
    def merge(self, left, right):
        result = []

        i = j = 0

        # Conqure
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
            
        # Add the remaining element of the array - which ever is remaining 
        result.extend(left[i : ])
        result.extend(right[j : ])
        
        return result

# 5. ================ ================ ================ Quick Sort ================ ================= =======================
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        startIdx = 0
        endIdx = n - 1
        self.quickSort(nums, startIdx, endIdx)

        return nums

    def quickSort(self, nums, startIdx, endIdx):
        # Check if there is only element in array
        if startIdx >= endIdx:
            return
        
        # Randomly pick pivot and swap it to the start
        randIdx = random.randint(startIdx, endIdx)
        self.swap(nums, startIdx, randIdx)
        
        # Pivot element
        pivot = startIdx
        left = startIdx + 1
        right = endIdx

        # Sort the array so that every element smaller than the pivot goes to its left and every element larger goes to its right. 
        while left <= right:
            if nums[left] > nums[pivot] and nums[right] < nums[pivot]:
                """
                If left ele is greater than pivot and right ele is smaller than pivot -> swap them
                why?
                because every element smaller than the pivot goes to its left and every element larger goes to its right.
                """
                self.swap(nums, left, right)
            
            # Adjust your pointers as per the rule
            if nums[left] <= nums[pivot]:
                left += 1
            
            if nums[right] >= nums[pivot]:
                right -= 1
        
        # place the pivot in its correct final position
        self.swap(nums, pivot, right)

        # Recursively apply quick sort on the left side and right side
        smaller_side = (right - 1) - startIdx <= endIdx - (right + 1)

        if smaller_side:
            self.quickSort(nums, startIdx, right - 1)
            self.quickSort(nums, right+1, endIdx)
        else:
            self.quickSort(nums, right+1, endIdx)
            self.quickSort(nums, startIdx, right - 1)
    

    def swap(self, nums, left, right):
        nums[left], nums[right] = nums[right], nums[left]