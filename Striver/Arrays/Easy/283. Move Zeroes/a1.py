'''
The 2 requirements of the question are:

    Move all the 0's to the end of array.

    All the non-zero elements must retain their original order.

It's good to realize here that both the requirements are mutually exclusive, 
i.e., you can solve the individual sub-problems and then combine them for the final solution.

'''


# ---------------- Copying ----------------

# Tc nad Sc: O(n)

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        ans = [0] * n

        j = 0
        for i in range(n):
            if nums[i] != 0:
                ans[j] = nums[i]
                j += 1
        
        nums[:] = ans[:]

        return nums
    

# ---------------- 2-Pointer ----------------

# Tc : O(n) | Sc: O(1)

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        j = 0
        for i in range(n):
            if nums[i] != 0:
                nums[j] , nums[i] = nums[i] , nums[j]
                j += 1 # keep track of where zero is - and next time swap that pos with non zero val

        return nums