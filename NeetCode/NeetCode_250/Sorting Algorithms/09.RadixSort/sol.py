"""
Radix Sort:
Followss Count Sort

Core Idea:
Sort numbers digit by digit, from least significant to most significant digit.
At each digit position, use counting sort (stable) to sort by that digit alone.
Stability ensures previous digit orderings are preserved as we move to the next digit.

TC: O(d * (n + b)) where d = number of digits, n = number of elements, b = base (10)
SC: O(n + b)
"""

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Separate negatives and non-negatives
        neg_num = [-x for x in nums if x < 0] # flip to positive for sorting
        pos_num = [x for x in nums if x >= 0]

        # Sort both parts using radix sort
        sorted_pos = self.radixSort(pos_num)
        sorted_neg = self.radixSort(neg_num)

        # Flip negatives back and reverse (largest negative = smallest number)
        sorted_neg = [-x for x in reversed(sorted_neg)]

        # Combine both negative and positive sorted array
        return sorted_neg + sorted_pos
    
    def radixSort(self, nums):
        """
        Unit place (1s pos) -> divide by 1
        Tens place (10s pos) -> divide by 10
        Hundreth place (100s pos) -> divide by 100
        Thousand place (1000s pos) -> divide by 1000
        """
        if not nums:
            return nums
        
        max_val = max(nums)

        #  # Sort digit by digit from LSD to MSD
        exp = 1

        while max_val // exp > 0:
            nums = self.countSort(nums, exp)
            exp *= 10 # move from right to left
        
        return nums
    
    def countSort(self, nums, exp):
        # Step 1: Count frequency of each digit at position exp
        count_freq = [0] * 10 # digits 0-9
        for num in nums:
            ele = (num // exp) % 10 # get element at that specific pos (unit, 10s etc)
            count_freq[ele] += 1
        
        # Step 2: Prefix sum — count[i] now holds position of this digit in output
        for i in range(1, 10):
            count_freq[i] = count_freq[i-1] + count_freq[i]
        
        # Step 3: Build output — reverse for stability
        output = [0] * len(nums)
        for i in reversed(range(len(nums))):
            ele = (nums[i] // exp) % 10 # get element at that specific pos (unit, 10s etc)
            idx = count_freq[ele] - 1
            output[idx] = nums[i]
            count_freq[ele] -= 1
        
        return output

