# Tc: O(2n) = O(n) | Sc: O(n)

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        atmost_k = self.subarray(nums, k)
        atmost_k_minus_one = self.subarray(nums, k - 1)

        return atmost_k - atmost_k_minus_one
    
    def subarray(self, nums, k):
        n = len(nums)

        total = 0

        left = right = 0

        freq = collections.defaultdict(int)

        while right < n:
            freq[nums[right]] += 1

            while len(freq) > k:
                freq[nums[left]] -= 1

                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                
                left += 1
            
            total += (right - left + 1)

            right += 1
        
        return total