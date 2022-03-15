# Time = O(n^2) Space = O(n)
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        dic = collections.defaultdict(int)
        
        length = len(nums)
        
        # add last two value in dic
        dic[ nums[length-1] - nums[length-2] ] = 1
        # print(dic)
        
        count = 0
        
        # Fix b and keep iterating a value
        for b in range(length - 3, 0, -1): # dont onot include 0
            # iterate for different value of a
            for a in range(b-1, -1, -1) :
                number = nums[a] + nums[b]
                # if a similar match a + b = d - c is found then increase count
                count += dic[number]
                
                
            # Now add new value to cache where c value = to b
            for d in range(length - 1, b , -1):
                number = nums[d] - nums[b]
                dic[number] += 1
                
        return count