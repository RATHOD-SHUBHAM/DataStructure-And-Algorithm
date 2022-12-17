'''

If s == 'H', return -1
If s starts with HH', return -1
If s ends with HH', return -1
If s has 'HHH', return -1

Each house H needs one bucket,
that's s.count('H')
Each 'H.H' can save one bucket by sharing one in the middle,
that's s.count('H.H') (greedy count without overlap)
So return s.count('H') - s.count('H.H')




'''

# Time O(n) | Space O(1)
class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        if hamsters == "H":
            return -1
    
        
        # if start and end is HH then it is not possible to feed
        if (hamsters[:2]  == "HH") or (hamsters[-2:] == "HH"):
            return -1
        
        # if anywhere in between we have 3 hamstrer together then we cant feed the center one
        if "HHH" in hamsters:
            return -1
        
        return hamsters.count("H") - hamsters.count("H.H")