class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort() # nlogn

        op = []

        k = 0

        while k < (n-2):
            # handle duplicate
            while k > 0 and k < n-2 and nums[k] == nums[k-1]:
                k += 1

            i = k + 1
            j = n - 1

            while i < j:
                cur_sum = nums[k] + nums[i] + nums[j]

                if cur_sum == 0:
                    op.append([nums[k] , nums[i] , nums[j]])

                    # This will handle index out of range
                    i += 1
                    j -= 1

                    # This will handle duolicate
                    while i < j and nums[i] == nums[i-1]:
                        i += 1
                    
                    while i < j and nums[j] == nums[j+1]:
                        j -= 1
                
                elif cur_sum < 0:
                    i += 1

                    while i < j and nums[i] == nums[i-1]:
                        i += 1
                
                else:
                    j -= 1

                    while i < j and nums[j] == nums[j+1]:
                        j -= 1

            k += 1
        
        return op