# Bucket Sort Explanation
'''
    Bucket Sort is a sorting algorithm that divides the unsorted array elements into several groups called buckets. 
    Each bucket is then sorted by using any of the suitable sorting algorithms or recursively applying the same bucket algorithm.
    Finally, the sorted buckets are combined to form a final sorted array.

'''

# Bucket Sort is a sorting algorithm that divides the unsorted array elements into several groups called buckets.

# Tc: O(nlogn) | Sc: O(nk)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # get the freq of nums
        freq = collections.defaultdict()

        for n in nums:
            if n not in freq:
                freq[n] = 1
            else:
                freq[n] += 1
        
        print(freq)

# We are dividing each element in a bucker called as frequency.