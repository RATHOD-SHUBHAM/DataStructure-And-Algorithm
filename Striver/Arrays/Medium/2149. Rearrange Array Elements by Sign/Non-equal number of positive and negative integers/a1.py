class Solution:
    def positiveNegative(self, nums):
        n = len(nums)

        positive = []
        negative = []

        for i in range(n):
            if nums[i] > 0:
                positive.append(nums[i])
            else:
                negative.append(nums[i])
        

        new_nums = [None] * n
        positive_len = len(positive)
        negative_len = len(negative)

        ns = min( positive_len,negative_len)

        for i in range(ns):
            new_nums[i * 2] = positive[i]
            new_nums[(i*2) + 1] = negative[i]


            if i == ns - 1:
                if positive_len > negative_len:
                    new_nums[:] = new_nums[ : ((i * 2) + 1) + 1] + positive[i+1 : ]
                    break
                else:
                    new_nums[:] = new_nums[ : ((i * 2) + 1) + 1] + negative[i+1 : ]
                    break
            
            

        return new_nums


if __name__ == '__main__':
    # arr = [1,2,-4,-5,3,4]
    arr = [1,2,-3,-1,-2,-3]
    obj = Solution()

    print(obj.positiveNegative(arr))



# ---------------Solution 2 ---------------------------------------

class Solution:
    def positiveNegative(self, nums):
        n = len(nums)

        positive = []
        negative = []

        for i in range(n):
            if nums[i] > 0:
                positive.append(nums[i])
            else:
                negative.append(nums[i])
        

        output = []

        p1 = 0
        p2 = 0

        while p1 < len(positive) and p2 < len(negative):
            output.append(positive[p1])
            p1 += 1

            output.append(negative[p2])
            p2 += 1

        if p1 < len(positive):
            output.extend(positive[p1:])
        
        if p2 < len(negative):
            output.extend(negative[p2:])
        
        return output


if __name__ == '__main__':
    # arr = [1,2,-4,-5,3,4]
    arr = [1,2,-3,-1,-2,-3]
    obj = Solution()

    print(obj.positiveNegative(arr))


# ---------------Solution 3 ---------------------------------------

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
            
            
