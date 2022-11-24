class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        k = 4
        return self.k_sum(nums , target , k)
    
    def k_sum(self, nums, target , k):
        print("nums: ",nums)
        print("target: ", target)
        print("k : ", k)
        
        res = []
        
        # base case
        if not nums:
            print("\n\n")
            return res
        
        # There are k remaining values to add to the sum. The 
        # average of these values is at least target // k.
        avg_sum = target // k
        print("average sum. : ", avg_sum)
        
        # We cannot obtain a sum of target if the smallest value
        # in nums is greater than target // k or if the largest 
        # value in nums is smaller than target // k.
        if avg_sum < nums[0] or avg_sum > nums[-1]:
            return res
        
        if k == 2:
            print(" k == 2")
            return self.two_sum(nums, target)
        
        for i in range(len(nums)):
            print("i : ", i)
            print("nums[i] : ",nums[i])
            if i == 0 or nums[i] != nums[i-1]:
                print("\n")
                print("passing on: ....")
                print("nums[i+1 : ]: ",nums[i+1 : ])
                print("target - nums[i] : ",target - nums[i])
                print("k - 1 : ", k - 1)
                print("\n")
                for pair in self.k_sum(nums[i+1 : ], target - nums[i], k - 1):
                    print("pair : ", pair)
                    res.append( [nums[i]] + pair)
                    
        return res
    
    def two_sum(self, nums, target):
        pair = []
        cache = {}
        
        print("two sum nums: ",nums)
        print("two sum target: ",target)
        
        for i in range(len(nums)):
            print("i: ",i)
            print("nums[i]: ",nums[i])
            
            diff = target - nums[i]
            print("diff: ",diff)
            
            print("pair: ",pair)
            # avoid duplicate value to be added
            if len(pair) == 0 or nums[i] != pair[-1][1]:
                if diff in cache:
                    pair.append([diff, nums[i]])
                    print("append paior: ", pair)
            '''
            # all the if condition will work adn they mean the same
            if diff in cache and ( len(pair) == 0 or nums[i] != pair[-1][1] ):
                pair.append([diff, nums[i]])


            or


            if diff in cache and ( len(pair) == 0 or nums[i] != nums[i-1] ):
                pair.append([diff, nums[i]])
            '''
                    
            cache[nums[i]] = i
            print("cache: ",cache)
            print("\n")
        
        # print(pair)
        return pair