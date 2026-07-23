"""
[num - valueDiff, num + valueDiff]
The math behind it

We want to find any x in the window such that abs(num - x) <= valueDiff. Expanding the absolute value:

abs(num - x) <= valueDiff
⟺  -valueDiff <= num - x <= valueDiff
⟺  num - valueDiff <= x <= num + valueDiff

So any value that could possibly match num must fall in the closed interval:

[num - valueDiff, num + valueDiff]

That's exactly what range = [num - valueDiff, num + valueDiff] is capturing — it's the "acceptable zone" around num. Anything in the sorted set that falls inside this interval is a valid match.


"""



class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        notepad = SortedSet()

        ptr = 0

        for num in nums:
            range = [num - valueDiff, num + valueDiff]
            
            pos = notepad.bisect_left(range[0])
            
            # If even this closest candidate fails the check abs(num - notepad[pos]) <= valueDiff, no other element could possibly pass either (everything else is farther away).
            if pos < len(notepad) and abs(num - notepad[pos]) <= valueDiff:
                return True
            
            notepad.add(num)

            if len(notepad) > indexDiff:
                notepad.remove(nums[ptr])
                ptr += 1
            
        return False


