# Tc and Sc: O(n)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        # Get the frequency(No of occurance) of each element
        freq = collections.Counter(nums)

        # Create a bucket to store values
        m = max(freq.values())

        freq_bucket = [[] for _ in range(m+1)]

        for key, value in freq.items():
            freq_bucket[value].append(key)
        

        # Return the K frequent element from bucket
        op = []
        for freq_ele in reversed(freq_bucket):
            for ele in freq_ele:
                op.append(ele)

                if len(op) == k:
                    return op