# Tc: O(n^3) | Sc: O(1)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)

        count = 0

        # Subarray boundary
        for i in range(n):
            for j in range(i , n):
                sum = 0
                # Calculate sum for the subarray
                for p in range(i, j+1):
                    sum += nums[p]
                
                if sum == k:
                    count += 1
        
        return count


# -------------------------- Prefix + Hashmap --------------------------

# Tc and Sc: O(n)

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # Prefix sum
        prefix_sum = [0] * n
        prefix_sum[0] = nums[0]

        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i-1] + nums[i]
        
        # Hashmap + Two sum
        dic = {0 :  1} # Sum of subarray : No of occurance of subarray with this sum

        count = 0
        
        for i in range(n):
            diff = prefix_sum[i] - k # Check if this is a subarray with sum k

            # If diff was seen at index j, then the subarray from j+1 to i has sum = k.
            if diff in dic:
                count += dic[diff] # Include all the subarray
            
            if prefix_sum[i] in dic:
                dic[prefix_sum[i]] += 1
            else:
                dic[prefix_sum[i]] = 1
        
        return count

# -------------------------- Prefix + Hashmap Single Pass--------------------------

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        # Hashmap + Two sum
        dic = {0 :  1} # Sum of subarray : No of occurance of subarray with this sum

        count = 0

        cur_sum = 0
        
        for i in range(n):
            # Two Sum
            cur_sum += nums[i]
            
            diff = cur_sum - k # Check if this is a subarray with sum k

            # If diff was seen at index j, then the subarray from j+1 to i has sum = k.
            if diff in dic:
                count += dic[diff] # Include all the subarray
            
            if cur_sum in dic:
                dic[cur_sum] += 1
            else:
                dic[cur_sum] = 1
        
        return count

            
