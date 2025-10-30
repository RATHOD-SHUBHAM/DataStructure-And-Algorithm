class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        nums.sort()
        print(nums)

        op = []

        '''
            If the current value is greater than zero, break from the loop. Remaining values cannot sum to zero
        '''

        for i in range(n):
            if nums[i] > 0:
                break
            
            if i == 0 or nums[i] != nums[i-1]:
                self.twoSum(i, op, nums)
        
        return op
    
    def twoSum(self, i, op, nums):

        left = i + 1
        right = len(nums) - 1

        while left < right:
            cur_sum = nums[i] + nums[left] + nums[right]

            if cur_sum < 0:
                left += 1
                

            elif cur_sum > 0:
                right -= 1

            
            else:
                op.append([nums[i] , nums[left] , nums[right]])

                left += 1
                right -= 1

                # we dont allow duplicate in the op array

                while left < right and nums[left] == nums[left - 1]:
                    left += 1

                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
        
        return op