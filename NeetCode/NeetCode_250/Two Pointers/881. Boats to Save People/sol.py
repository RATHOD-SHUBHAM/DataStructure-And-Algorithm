# Tc: O(nlogn) | Sc: O(n)

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        n = len(people)

        i = 0
        j = n - 1

        count = 0

        while i <= j:

            # Even without this block the logic will go to else conidtion and break out
            # if i == j:
            #     count += 1
            #     return count

            cur_weight = people[i] + people[j]

            if cur_weight > limit:
                # assign one boat to only this one person
                # count += 1
                j -= 1
            else:
                # assign one boat to both the persons
                # count += 1
                i += 1
                j -= 1
            
            count += 1
    
        return count

# ================================== Using Counting Sort ==================================

"""
since people[i] <= limit <= 3*10^4, counting sort works great here and gets you to O(n + limit) instead of O(n log n)

Since limit <= 3 * 10^4 is a fixed constant bound (not growing with n), as n gets large, O(n + limit) behaves like O(n) — linear — while O(n log n) keeps growing faster. So yes, time complexity improves, especially for large n.
Concretely: if n = 50,000 (max per constraints):

n log n ≈ 50,000 × log₂(50,000) ≈ 50,000 × 15.6 ≈ 780,000 operations
n + limit ≈ 50,000 + 30,000 = 80,000 operations

So roughly 10x fewer operations in the worst case.

Tc and Sc: Total: O(n + limit)
"""

class Solution:
    def countsort(self, nums, limit):
        n = len(nums)

        # freq bucket needs to be sized using the maximum possible value in the array (i.e. limit, or max(nums)
        freq = [0] * (limit + 1)

        for i in range(n):
            val = nums[i]
            freq[val] += 1
        

        sorted_array = []
        for weight in range(len(freq)):
            sorted_array.extend([weight] * freq[weight])
        
        return sorted_array
        


    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people = self.countsort(people, limit)

        n = len(people)

        i = 0
        j = n - 1

        count = 0

        while i <= j:

            # Even without this block the logic will go to else conidtion and break out
            # if i == j:
            #     count += 1
            #     return count

            cur_weight = people[i] + people[j]

            if cur_weight > limit:
                # assign one boat to only this one person
                # count += 1
                j -= 1
            else:
                # assign one boat to both the persons
                # count += 1
                i += 1
                j -= 1
            
            count += 1
    
        return count

