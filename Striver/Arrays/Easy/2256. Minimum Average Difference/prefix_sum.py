class Solution:
    def totalAverage(self, arr1: List[int], arr1_len:int , arr2: List[int], arr2_len:int) -> int:
        arr1_avg = arr1 // arr1_len
        
        arr2_avg = 0
        if arr2_len > 0:
            arr2_avg = arr2 // arr2_len

        total_avg_difference = abs(arr1_avg - arr2_avg)
        return total_avg_difference

    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)

        first_half_sum = nums[0]
        first_half_len = 1

        second_half_sum = sum(nums[1 : ])
        second_half_len = n - 1

        total_avg = self.totalAverage(first_half_sum, first_half_len, second_half_sum, second_half_len)

        min_avg = total_avg

        idx = 0

        for i in range(1, n):
            first_half_sum += nums[i]
            first_half_len += 1

            second_half_sum -= nums[i]
            second_half_len -= 1

            total_avg = self.totalAverage(first_half_sum, first_half_len, second_half_sum, second_half_len)

            if total_avg < min_avg:
                min_avg = total_avg
                idx = i
        
        return idx


# ------------------  Same Solution ------------------

class Solution:
    def totalAverage(self, arr1: List[int], arr1_len:int , arr2: List[int], arr2_len:int) -> int:
        arr1_avg = arr1 // arr1_len
        
        arr2_avg = 0
        if arr2_len > 0:
            arr2_avg = arr2 // arr2_len

        total_avg_difference = abs(arr1_avg - arr2_avg)
        return total_avg_difference

    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)

        first_half_sum = 0
        first_half_len = 0

        second_half_sum = sum(nums)
        second_half_len = 0

        total_avg = 0

        min_avg = math.inf

        idx = 0

        for i in range(n):
            first_half_sum += nums[i]
            first_half_len = i + 1

            second_half_sum -= nums[i]
            second_half_len = n - i- 1

            total_avg = self.totalAverage(first_half_sum, first_half_len, second_half_sum, second_half_len)

            if total_avg < min_avg:
                min_avg = total_avg
                idx = i
        
        return idx     