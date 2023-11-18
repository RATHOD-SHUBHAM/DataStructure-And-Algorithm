# Bucket Sort - Because the answer is guranted to be unique
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Get count of numbers
        counter = collections.Counter(nums)
        # print(counter)

        # Step 2: add them to frequency table
        freq_lst = [[] for _ in range(len(nums) + 1)]
        # print(freq_lst)

        for num , count in counter.items():
            freq_lst[count].append(num)
        print(freq_lst)

        # step 3: get top k elemennt
        top_k = []
        for i in reversed(range(len(freq_lst))):
            for ele in freq_lst[i]:
                top_k.append(ele)
            
            if len(top_k) == k:
                break
        
        return top_k