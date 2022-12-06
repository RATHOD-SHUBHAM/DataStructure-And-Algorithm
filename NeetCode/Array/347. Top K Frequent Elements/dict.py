class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        counter = {}
        bucket = [[] for _ in range (n + 1)]
        
        for i in range(n):
            counter[nums[i]] = counter.get(nums[i] , 0) + 1
            
        for key , val in counter.items():
            bucket[val].append(key)
            
        k_freq = []
        
        for i in reversed(range(len(bucket))):
            ele = bucket[i]
            
            for item in ele:
                k_freq.append(item)
                
                if len(k_freq) == k:
                    return k_freq