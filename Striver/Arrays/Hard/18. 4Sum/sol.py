class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        n = len(nums)

        op = []

        # 4 sum
        for i in range(n):
            if i == 0 or nums[i] != nums[i-1]:
                self.threeSum(i, target, op, nums)
        
        return op
    
    def threeSum(self, parentIdx, target, op, nums):
        n = len(nums)

        for i in range(parentIdx + 1, n):
            if i == parentIdx + 1 or nums[i] != nums[i-1]:
                self.twoSum(parentIdx, i, op, target, nums)

        return
    
    def twoSum(self, parentIdx, idx, op, target, nums):
        n = len(nums)

        left = idx + 1
        right = n - 1

        while left < right:
            cur_sum = nums[left] + nums[right] + nums[parentIdx] + nums[idx]

            if cur_sum < target:
                left += 1
            elif cur_sum > target:
                right -= 1
            else:
                op.append((nums[left] , nums[right] , nums[parentIdx] , nums[idx]))

                left += 1
                right -= 1

                while left < right and nums[left] == nums[left - 1]:
                    left += 1

                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
        
        return op