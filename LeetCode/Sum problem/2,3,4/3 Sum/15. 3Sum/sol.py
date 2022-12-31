class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        triplets = []
        n = len(nums)
        
        for i in range(n):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            
            a = nums[i]
            
            left = i + 1
            right = n -1
            
            while left < right:
                b = nums[left]
                c = nums[right]
                
                target = a + b + c
                
                if target == 0:
                    triplets.append([a , b, c])
                    left +=1
                    right -= 1
                    
                    # check duplicates
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                        
                elif target < 0:
                    left += 1
                    # we can do this but anyways we wont get the sum = 0; so we can ignore
                    # while left < right and nums[left] == nums[left - 1]:
                    #     left += 1
                    
                else:
                    right -= 1
                    # while left < right and nums[right] == nums[right + 1]:
                    #     right -= 1
                    
        return triplets