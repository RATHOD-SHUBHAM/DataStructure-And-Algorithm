class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        count = 0
        nums.sort()
        print(nums)
        n = len(nums)
        
        for i in range(n):
            a = nums[i]
            
            left = i + 1
            right = n - 1
            
            while left < right:
                b = nums[left]
                c = nums[right]
                
                summ = a + b + c
                
                if summ < target:
                    # all the number btn left and right when added with left will be less than target
                    count += right - left
                    left += 1
                else:
                    right -= 1
                    
        return count