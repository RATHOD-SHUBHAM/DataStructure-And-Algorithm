# First learn the basic counting sort algorithm, then handle negative numbers.

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Step 1: Count the frequency of each element
        max_val = max(nums)
        count_freq = [0] * (max_val+1)
        for ele in nums:
            count_freq[ele] += 1
        
        # print(count_freq)
    
        # Step 2: Convert the count in posistion - Prefix sum
        for i in range(1, max_val+1):
            count_freq[i] = count_freq[i-1] + count_freq[i]
        
        # print(count_freq)

        # Step 3: Build the sorted array using prefix sum
        output = [0] * n
        for i in reversed(range(n)):
            ele = nums[i]
            idx = count_freq[ele] - 1 # prefix_sum[ele] stores a count (how many elements ≤ ele), but you need an index (0-based) so -1 does that for us.
            output[idx] = ele
            count_freq[ele] -= 1  # Move pointer left for next duplicate
        
        # print(output)

        return output
    

# -----------------------------------------------------------------------------------------------------

## Handle Negative numbers
'''
ele - min_val : this will make sure that smallest element's index will start from 0.
eg: [4, -1, -2, 2, 1, 0]
idx of -2 will be 0:
-2 - (-2) = -2 + 2 = 0
'''

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Handle Negative numbers
        min_val = min(nums)
        max_val = max(nums)
        range_val = max_val - min_val

        # Step 1: Count the frequency of each element
        count_freq = [0] * (range_val+1)
        for ele in nums:
            count_freq[ele-min_val] += 1
        
        # print(count_freq)
    
        # Step 2: Convert the count in posistion - Prefix sum
        for i in range(1, range_val+1):
            count_freq[i] = count_freq[i-1] + count_freq[i]

        # Step 3: Build the sorted array using prefix sum
        output = [0] * n
        for i in reversed(range(n)):
            ele = nums[i]
            idx = count_freq[ele - min_val] - 1 # prefix_sum[ele] stores a count (how many elements ≤ ele), but you need an index (0-based) so -1 does that for us.
            output[idx] = ele
            count_freq[ele-min_val] -= 1  # Move pointer left for next duplicate
        
        # print(output)

        return output