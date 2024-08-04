# ---------------- 2 Pass ----------------

# Tc: O(2n) | Sc: O(n)

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        positive = []
        negative = []

        # Store all the positive and negative number
        for i in range(n):
            if nums[i] > 0:
                positive.append(nums[i])
            else:
                negative.append(nums[i])
        

        # Place them at the right Index
        new_nums = [None] * n
        for i in range(len(positive)):
            new_nums[i * 2] = positive[i]
            new_nums[(i*2) + 1] = negative[i]
        
        return new_nums
    
# ---------------- 1 Pass ----------------

# Tc: O(2n) | Sc: O(n)

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Place them at the right Index
        new_nums = [None] * n

        positive_Index = 0
        negative_Index = 1

        for i in range(n):
            if nums[i] > 0:
                new_nums[positive_Index] = nums[i]
                positive_Index += 2
            else:
                new_nums[negative_Index] = nums[i]
                negative_Index += 2
        
        return new_nums
    

# ---------------- Pointer - works for unequal length ---------------- 

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        positive = 0
        while positive < n:
            if nums[positive] > 0:
                break
            
            positive += 1
        
        negative = 0
        while negative < n:
            if nums[negative] < 0:
                break
            
            negative += 1
        
        op = []
        
        while positive < n or negative < n:
            # Append the numbers
            if positive < n:
                op.append(nums[positive])
            
            if negative < n:
                op.append(nums[negative])

            # Move the pointers
            while positive < n:
                
                positive += 1

                # if positive >= n:
                #     break
                
                if positive >= n or nums[positive] > 0:
                    break
            
            while negative < n:
                
                negative += 1

                # if negative >= n:
                #     break
                
                if negative >= n or nums[negative] < 0:
                    break
                
        return op
            
            
