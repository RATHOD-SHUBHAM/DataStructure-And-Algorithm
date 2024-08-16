#  --------------------  Exact K  --------------------


'''
Assume:
    Convert every odd to 1 and every even to 0

'''
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        atmost_k = self.subarraySum(nums, k)
        # print(atmost_k)
        atmost_k_minus_one = self.subarraySum(nums, k - 1)
        # print(atmost_k_minus_one)

        return atmost_k - atmost_k_minus_one
    
    def subarraySum(self, nums, k):
        n = len(nums)

        left = right = 0

        total = cur_sum = 0

        while right < n:
            # check if odd number
            if nums[right] % 2 != 0:
                cur_sum += 1
            
            while left <= right and cur_sum > k:
                if nums[left] % 2 != 0:
                    cur_sum -= 1
                
                left += 1
            
            total += (right - left) + 1
        
            right += 1
        
        return total



#  --------------------  Prefix Sum  --------------------


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)

        dic = {0:1}

        cur_sum = total = 0

        for i in range(n):
            if nums[i] % 2 != 0:
                cur_sum += 1
            
            diff = cur_sum - k

            if diff in dic:
                total += dic[diff]
            
            if cur_sum in dic:
                dic[cur_sum] += 1
            else:
                dic[cur_sum] = 1
        
        return total