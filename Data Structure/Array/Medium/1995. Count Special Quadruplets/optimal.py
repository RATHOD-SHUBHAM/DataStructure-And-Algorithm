# Time = O(n^2) Space = O(n)
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        res = 0
        
        count = defaultdict(int)
        
        count[nums[len(nums)-1] - nums[len(nums)-2]] = 1
        print(count)
        
        for b in range(len(nums) - 3, 0, -1):
            print("nums[b] : ",nums[b])
            for a in range(b - 1, -1, -1):
                # Check if  a + b in count. If it is there. Increase count by that number
                res += count[nums[a] + nums[b]]
            
            for x in range(len(nums) - 1, b, -1):
                print("nums[x] : ",nums[x])
                count[nums[x] - nums[b]] += 1
                print("count: ", count)
            print("\n")
        
        return res