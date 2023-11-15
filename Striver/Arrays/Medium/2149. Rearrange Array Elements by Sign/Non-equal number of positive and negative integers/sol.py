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



