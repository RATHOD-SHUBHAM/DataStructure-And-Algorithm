# Tc: O(n!) | Sc: O(n)
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        # perform permutation
        all_permutations = []
        
        def backTrack(i):
            if i == n:
                if nums not in all_permutations:
                    all_permutations.append(nums[:])
                return 
            
            for j in range(i, n):
                nums[i] , nums[j] = nums[j] , nums[i]

                backTrack(i+1)

                nums[i] , nums[j] = nums[j] , nums[i]

        # Main -----------------------------------------
        
        backTrack(0)

        # get the lexicographical order
        all_permutations.sort()

        # Return the next index of nums
        idx_of_arr = all_permutations.index(nums)


        if idx_of_arr + 1 < n:
            nums[:] = all_permutations[idx_of_arr + 1]
        
            return nums
        else:
            nums[:] = all_permutations[0]

            return nums

        