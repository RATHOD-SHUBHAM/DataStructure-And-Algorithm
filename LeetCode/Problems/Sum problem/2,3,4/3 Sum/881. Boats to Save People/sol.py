# Tc: O(nlogn) ; Sc: O(n)
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        minimum_no_of_boat = 0
        people.sort()
        n = len(people)
        
        left = 0
        right = n - 1
        
        while left <= right:
            # if there is just one person
            if left == right and people[left] <= limit:
                minimum_no_of_boat += 1
                left += 1
                right -= 1
                break
            
            total_weight = people[left] + people[right]

            # If the weight is more: then heaviest person require one boat
            if total_weight > limit:
                minimum_no_of_boat += 1
                right -= 1
            
            # if boat is less than limit: we anyways can put just 2 memeber on baot
            # so move the pointer by increasing the counter
            elif total_weight <= limit:
                minimum_no_of_boat += 1
                left += 1
                right -= 1
                
                
        return minimum_no_of_boat