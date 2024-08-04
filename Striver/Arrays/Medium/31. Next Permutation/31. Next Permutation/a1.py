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
            # return all_permutations[idx_of_arr + 1] # this can also be copied to nums array
            nums[:] = all_permutations[idx_of_arr + 1]
        
            return nums
        else:
            nums[:] = all_permutations[0]

            return nums

#  ------------------------------  Optimal  ------------------------------

'''
   - There is a inbuilt library in C++ called as nextpermutation

   This is a implementation of that using python

   - This is a trick that we can know only after practise
'''


'''
# 1. Finding Breakpoint
    First, we observe that for any given sequence that is in descending order, no next larger permutation is possible.


# 2. Find the immediate greater element

# 3. Sort the remaining element
'''

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        # Step 1: Find Break Point
        '''
            We start from the back , because in general, when we sort the value, we usually compare the right most value and move left.
        '''
        pivotIdx = -1
        for i in reversed(range(n-1)):
            if nums[i] < nums[i+1]:
                pivotIdx = i # break point found
                break
        
        print(pivotIdx)

        # Edge case: When this is the last possible permuted value,
        # There cant be a next lexicographically permutation
        if pivotIdx == -1:
            # print(reversed(nums))
            return nums.reverse()

        # Step 2: Find the immediate next greater element to pivot 
        '''
            Find a value that is greater than the break point but lesser that then remaining value.
        '''
        for i in reversed(range(pivotIdx, n)):
            # based on the graph we can see that we can cleverly swap the values.
            if nums[i] > nums[pivotIdx]:
                # swap value
                nums[i], nums[pivotIdx] = nums[pivotIdx] , nums[i]
                break
        # print(nums)

        # Step 3: Sort the element after pivot idx
        nums[pivotIdx + 1 : ] = reversed(nums[pivotIdx + 1 : ])

        # print(nums)

        return nums