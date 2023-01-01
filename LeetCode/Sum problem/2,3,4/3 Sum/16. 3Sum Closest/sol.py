class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        
        min_diff = math.inf
        closest_sum = 0
        
        for i in range(n):
            a = nums[i]
            
            left = i + 1
            right = n -1
            
            while left < right:
                b = nums[left]
                c = nums[right]
                
                summ = a + b + c
                
                # calculate the min sum
                diff = summ - target
                if abs(diff) <= min_diff:
                    min_diff = abs(diff)
                    closest_sum = summ
                    
                if summ < target:
                    left += 1
                elif summ > target:
                    right -= 1
                else:
                    # summ == target: diff is 0 this will be the closest
                    break

        
        return closest_sum
                    