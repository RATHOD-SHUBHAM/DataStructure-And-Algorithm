class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count the frequence of each element
        freq_counter = collections.Counter()
        
        for i in range(len(nums)):
            freq_counter[nums[i]] += 1
            
        # add them to a bucket
        bucket = [[] for _ in range(len(nums) + 1)]
        
        for ele, freq in freq_counter.items():
            bucket[freq].append(ele)
            
        # get the k freq
        k_freq_ele = []
        
        for i in reversed(range(len(bucket))):
            ele = bucket[i]
            
            for j in ele:
                k_freq_ele.append(j)
                
                if len(k_freq_ele) == k:
                    return k_freq_ele