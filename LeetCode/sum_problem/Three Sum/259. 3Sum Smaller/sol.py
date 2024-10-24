class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)

        count = 0

        for i in range(n):

            left = i + 1 
            right = n - 1

            while left < right:
                cur_sum = nums[i] + nums[left] + nums[right]

                if cur_sum < target:
                    count += 1
                    # we know all the elements in between will also result in sum less than target.
                    count += (right - left - 1) 
                    left += 1
                else:
                    right -= 1

        return count 