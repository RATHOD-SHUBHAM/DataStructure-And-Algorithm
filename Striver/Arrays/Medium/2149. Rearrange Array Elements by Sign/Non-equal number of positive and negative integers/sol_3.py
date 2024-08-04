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
            
            
