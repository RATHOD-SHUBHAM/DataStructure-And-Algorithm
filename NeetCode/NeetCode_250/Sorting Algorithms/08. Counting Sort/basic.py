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