class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)

        total_avg = 0

        min_avg = math.inf

        idx = 0

        first_half_sum = 0

        for i in range(n):
            first_half_sum += nums[i]
            first_half_len = i + 1 # len of first half of elements

            # Compute the sum of second half
            second_half_sum = 0
            for j in range(i+1, n):
                second_half_sum += nums[j]
            
            second_half_len = n - i - 1 # len of second half of elements

            # Compute average of first and second half
            first_half_avg = first_half_sum // first_half_len

            sec_half_avg = 0 
            if second_half_sum > 0:
                '''
                Hadling situation where there is no second half
                '''
                sec_half_avg = second_half_sum // second_half_len

            total_avg = abs(first_half_avg - sec_half_avg)

            if total_avg < min_avg:
                min_avg = total_avg
                idx = i
        
        return idx
    

# ------------------- Same solution with built in -------------------

class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)

        total_avg = 0

        min_avg = math.inf

        idx = 0

        for i in range(n):
            first_half_sum = sum(nums[ : i + 1])
            first_half_len = i + 1 # len of first half of elements

            # Compute the sum of second half
            second_half_sum = sum(nums[i+1 : ])
            second_half_len = n - i - 1 # len of second half of elements

            # Compute average of first and second half
            first_half_avg = first_half_sum // first_half_len

            sec_half_avg = 0 
            if second_half_sum > 0:
                '''
                Hadling situation where there is no second half
                '''
                sec_half_avg = second_half_sum // second_half_len

            total_avg = abs(first_half_avg - sec_half_avg)

            if total_avg < min_avg:
                min_avg = total_avg
                idx = i
        
        return idx
        
        