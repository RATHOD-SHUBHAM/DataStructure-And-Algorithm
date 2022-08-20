class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_freq = {}
        
        bucket = [[] for _ in range(len(nums) + 1)]
        
        for num in nums:
            count_freq[num] = 1 + count_freq.get(num , 0)
            
        for key , val in count_freq.items():
            bucket[val].append(key)
            
        res = []
        for ele in reversed(range(len(bucket))):
            for i in bucket[ele]:
                res.append(i)
                
                if len(res) == k:
                    return res